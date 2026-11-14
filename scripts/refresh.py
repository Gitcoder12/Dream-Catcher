#!/usr/bin/env python3
"""Refresh public repository metadata and configured official RSS/Atom feeds.

Private repositories are never requested or written to this public repository.
Feed imports preserve source links and are marked for human review.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OWNER = "Gitcoder12"
TODAY = date.today().isoformat()
USER_AGENT = "Dream-Catcher-Research-Refresh/1.0"
MAX_FEED_ITEMS = 20
TIMEOUT = 25

UPDATE_FIELDS = [
    "update_id", "company_id", "published_date", "checked_date",
    "update_title", "summary", "source_url", "source_type", "evidence_status"
]
REPO_FIELDS = [
    "repo_full_name", "repo_url", "description", "primary_language",
    "stars", "forks", "open_issues", "default_branch", "visibility",
    "archived", "created_at", "updated_at", "pushed_at", "last_checked"
]
STATUS_FIELDS = [
    "source_id", "source_name", "source_url", "last_checked",
    "status", "items_seen", "items_added", "error_summary"
]


def fetch_bytes(url: str, accept: str = "*/*") -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": accept}
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return response.read(5_000_001)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fields})
    temp.replace(path)


def clean_text(value: str, limit: int = 500) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit]


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, names: set[str]) -> str:
    for child in list(element):
        if local_name(child.tag) in names:
            text = "".join(child.itertext()).strip()
            if text:
                return text
    return ""


def item_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.date().isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.date().isoformat()
    except ValueError:
        return ""


def parse_feed(payload: bytes, base_url: str) -> list[dict[str, str]]:
    root = ET.fromstring(payload)
    entries = [
        node for node in root.iter()
        if local_name(node.tag) in {"item", "entry"}
    ]
    result = []
    for entry in entries[:MAX_FEED_ITEMS]:
        title = clean_text(child_text(entry, {"title"}), 240)
        link = ""
        for node in list(entry):
            if local_name(node.tag) == "link":
                href = node.attrib.get("href", "").strip()
                rel = node.attrib.get("rel", "alternate")
                if href and rel in {"alternate", ""}:
                    link = href
                    break
                if node.text and node.text.strip() and not link:
                    link = node.text.strip()
        link = urllib.parse.urljoin(base_url, link)
        published = child_text(entry, {"pubdate", "published", "updated", "date"})
        published = item_date(published)
        summary = clean_text(child_text(
            entry, {"description", "summary", "content", "encoded"}
        ), 450)
        if title and link.startswith(("https://", "http://")) and published:
            result.append({
                "title": title,
                "link": link,
                "published": published,
                "summary": summary
            })
    return result


def refresh_repositories() -> tuple[int, str]:
    repositories: list[dict[str, object]] = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/users/{OWNER}/repos"
            f"?type=public&per_page=100&page={page}&sort=updated"
        )
        payload = json.loads(fetch_bytes(
            url, "application/vnd.github+json"
        ).decode("utf-8"))
        if not isinstance(payload, list):
            raise RuntimeError("GitHub public repository API returned an unexpected response")
        for repo in payload:
            # Explicit allow-list: never write private repository records.
            if repo.get("private") is not False:
                continue
            full_name = repo.get("full_name", "")
            if not full_name.startswith(f"{OWNER}/"):
                continue
            repositories.append({
                "repo_full_name": full_name,
                "repo_url": repo.get("html_url", ""),
                "description": clean_text(repo.get("description") or "", 350),
                "primary_language": repo.get("language") or "",
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "open_issues": repo.get("open_issues_count", 0),
                "default_branch": repo.get("default_branch", ""),
                "visibility": "public",
                "archived": str(bool(repo.get("archived", False))).lower(),
                "created_at": repo.get("created_at", ""),
                "updated_at": repo.get("updated_at", ""),
                "pushed_at": repo.get("pushed_at", ""),
                "last_checked": TODAY,
            })
        if len(payload) < 100:
            break
        page += 1
        if page > 10:
            raise RuntimeError("Repository pagination safety limit exceeded")
    repositories.sort(key=lambda item: str(item["repo_full_name"]).lower())
    write_csv(DATA / "repos.csv", REPO_FIELDS, repositories)
    return len(repositories), url


def refresh_feeds() -> tuple[int, int, list[dict[str, object]]]:
    updates_path = DATA / "updates.csv"
    existing = read_csv(updates_path)
    if existing and list(existing[0].keys()) != UPDATE_FIELDS:
        raise RuntimeError("data/updates.csv columns do not match the expected schema")
    seen_urls = {row.get("source_url", "") for row in existing}
    feeds = read_csv(DATA / "feeds.csv")
    status_rows: list[dict[str, object]] = []
    added = 0
    checked_sources = 0

    for feed in feeds:
        if str(feed.get("enabled", "")).lower() != "true":
            continue
        checked_sources += 1
        feed_url = feed.get("feed_url", "")
        company_id = feed.get("company_id", "")
        company_name = feed.get("company_name", "")
        try:
            payload = fetch_bytes(feed_url, "application/rss+xml, application/atom+xml, application/xml, text/xml")
            entries = parse_feed(payload, feed_url)
            source_type = (
                "official_atom_feed" if feed.get("feed_type") == "atom"
                else "official_rss_feed"
            )
            source_added = 0
            for entry in entries:
                if entry["link"] in seen_urls:
                    continue
                digest = hashlib.sha256(
                    f"{company_id}|{entry['link']}".encode("utf-8")
                ).hexdigest()[:12]
                existing.append({
                    "update_id": f"feed-{company_id}-{digest}",
                    "company_id": company_id,
                    "published_date": entry["published"],
                    "checked_date": TODAY,
                    "update_title": entry["title"],
                    "summary": entry["summary"],
                    "source_url": entry["link"],
                    "source_type": source_type,
                    "evidence_status": "feed_imported_needs_review",
                })
                seen_urls.add(entry["link"])
                source_added += 1
            added += source_added
            status_rows.append({
                "source_id": company_id,
                "source_name": company_name,
                "source_url": feed_url,
                "last_checked": TODAY,
                "status": "ok",
                "items_seen": len(entries),
                "items_added": source_added,
                "error_summary": "",
            })
        except Exception as error:  # preserve last known good data on source failure
            status_rows.append({
                "source_id": company_id,
                "source_name": company_name,
                "source_url": feed_url,
                "last_checked": TODAY,
                "status": "failed_using_last_saved_data",
                "items_seen": 0,
                "items_added": 0,
                "error_summary": clean_text(str(error), 180),
            })

    write_csv(updates_path, UPDATE_FIELDS, existing)
    write_csv(DATA / "refresh_status.csv", STATUS_FIELDS, status_rows)
    return checked_sources, added, status_rows


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    repo_count, repo_url = refresh_repositories()
    feed_count, update_count, feed_status = refresh_feeds()
    failures = sum(1 for row in feed_status if row["status"] != "ok")
    print(f"Public repositories refreshed: {repo_count}")
    print(f"Official company feeds checked: {feed_count}")
    print(f"New feed items added for review: {update_count}")
    print(f"Feed failures (previous data preserved): {failures}")
    print(f"Repository source: {repo_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
