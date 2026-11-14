# Work Notes — Dream-Catcher

**Maintainer:** Dharavath Satvik  
**Last updated:** 2026-11-14  
**Status:** Active maintenance — one persistent review branch

## Purpose

Dream-Catcher is a personal career-intelligence workspace. It tracks target employers, public company work, official hiring channels, publicly credited professional leaders/recruiting contacts, role families and evidence-backed portfolio fit.

It is a research aid, not an applicant-tracking system, employee database, endorsement record or claim of company relationships.

## Canonical file map

| Path | Single responsibility | Source of truth |
|---|---|---|
| `companies.md` | Human-readable overview of target companies and their official entry points | `data/companies.csv` |
| `data/companies.csv` | One canonical row per employer/company group | Company identity and official URLs |
| `data/updates.csv` | Dated, source-linked public company announcements | Official company newsroom/blog |
| `data/people.csv` | Publicly documented leaders and credited project authors | Official bios or public project credits |
| `data/careers.csv` | Official careers portals and public recruiting channels | Company-owned careers pages |
| `data/recruiters.csv` | Named recruiters only when their public recruiting role is verified | Public professional profile plus company-linked source |
| `repo-fit.md` | Provisional portfolio skills-fit mapping | Exact repository links; validate code before applications |
| `work-notes.md` | AI decisions, work log, limitations and next actions | Append dated entries here |

## No duplicate-document policy

- Do not recreate `COMPANY_INDEX.md`, `COMPANY_FIT.md`, `OPPORTUNITY_MAP.md` or a second `COMPANY_INTELLIGENCE.md`. Their useful scope is consolidated into the canonical files above.
- Do not put AI-generated sections, status notes or navigation lists in `README.md`.
- Do not maintain a second company list in prose when the canonical CSV already contains the records.
- Add updates as rows to `data/updates.csv`; do not create a new weekly/monthly file for every refresh.
- Add named recruiters only to `data/recruiters.csv` when their recruiting role and public profile are explicitly verified. General careers portals belong in `data/careers.csv`.

## Evidence and privacy rules

1. Prefer official company newsrooms, engineering/research blogs, leadership pages and careers sites.
2. Store the publication date separately from the date checked. If a source gives only a month, preserve month precision rather than inventing a day.
3. Keep the original source URL. Summaries must not claim more than the source.
4. Mark unverified or ambiguous fields as unknown; never guess a recruiter, email, job opening, title, salary, location or hiring status.
5. Use public professional information only. No private phone numbers, private email addresses, private messages, personal-life data, employee dossiers, leaks or confidential material.
6. Do not bypass login walls, scraping restrictions or access controls. X/LinkedIn following imports are not required for this project.
7. A company-to-repository mapping is a fit hypothesis, never proof of adoption, partnership, endorsement or hiring interest.
8. A role family is not a live vacancy. A careers portal is not evidence that a particular job is open.
9. Preserve upstream licences and authorship for portfolio forks.
10. Keep historical research snapshots. Never silently rewrite a past update to make it appear current.

## Update workflow

1. Check the official news/research pages for each target company.
2. Add only new, relevant announcements; skip routine marketing and duplicate syndication.
3. Verify each source URL opens and that the publication date/title match.
4. Record the checked date as `2026-11-14` (or the actual future check date).
5. Review current career pages separately; do not infer recruiter names from generic job pages.
6. Update the CSVs and this work log in the same branch/PR.
7. Review duplicate company IDs, malformed CSV rows, empty source URLs and stale dates before requesting review.

## Current status — 2026-11-14

- PR #2 was merged on 2026-11-14. Its working branch remains available and is the only side branch used for the next review cycle.
- All Dream-Catcher edits stay on `research/social-company-import-foundation`; do not create another side branch.
- X/LinkedIn follow lists are out of scope. The update feed currently has 23 sourced entries covering all 21 company groups; it is a seed snapshot, not an exhaustive historical archive.
- No recruiter identities have been invented. The recruiting-channel file records official application routes; `data/recruiters.csv` is the dedicated recruiter register and currently contains only its schema because no individual recruiter record has yet been verified from an official/public professional source.
- The README now explains the project in simple language and links to the core data files.

## Public and private repository rules

- The public repository inventory contains public repositories only. It includes public archived repositories with `archived=true`.
- Private repositories are not deleted, changed or listed by name in this public project. This protects their visibility and contents.
- The company fit matrix contains only active public repositories. Archived public projects remain in the inventory for preservation, not as active targets.
- A visibility/archival check found 13 private repositories and 2 archived public repositories among the 61 accessible account repositories on 2026-11-14.

## Interview practice

- `data/interviews.csv` contains 42 original practice prompts: one core and one hard prompt for each of the 21 employer groups.
- These are company-aligned learning exercises, not verified company favourites or leaked interview questions.
- Every row provides a recommended solution, two alternative approaches, complexity/trade-offs, edge cases and follow-up questions.
- Keep new prompts original, cite the official company domain page for the technical area, and do not claim a question was asked by a company without reliable public evidence.

## Automated refresh

- `scripts/refresh.py` refreshes public GitHub repository metadata and imports items from enabled official RSS/Atom feeds.
- `data/feeds.csv` lists all 21 employer groups. Only configured official feeds are fetched; companies without a verified feed remain manual.
- Imported feed items keep their original source URL and are marked `feed_imported_needs_review`; no AI-generated summary is invented.
- Source failures preserve the previous data and are recorded in `data/refresh_status.csv`.
- `.github/workflows/refresh.yml` is scheduled daily at 04:30 UTC and can also be run manually. It writes only to `research/social-company-import-foundation`, never to `main`.
- GitHub scheduled runs start only after this workflow is merged into the default branch. Until then, it can be run manually from the side branch after the workflow file exists there.

## Work log

### 2026-11-14 — Canonical consolidation
- Replaced the overlapping company-index/intelligence/fit documents with one company directory and one canonical company CSV.
- Added a dated public updates feed, public people register and official recruiting-channel register.
- Kept the 61-row repository-fit matrix as a provisional mapping, not a functionality certification.
- Moved AI-maintained notes into this file and removed the AI addendum from README.
- PR #1 was closed after its useful research was preserved in this canonical structure.
- Validation performed: source/link spot-checks and structural CSV review. No application build or runtime tests apply to this documentation/data-only change.

### Branch and review rule
- Use only `research/social-company-import-foundation` for all follow-up work.
- Make one focused change per user prompt, commit it to this branch, validate it, and stop for the user's review.
- Do not create another side branch, merge the PR, or change `main` without an explicit request.

### 2026-11-14 — Repository visibility and interview bank
- Removed private and archived repositories from the active public company-fit matrix. No repository was deleted or changed.
- Added a public repository inventory with visibility and archived flags; private repository names are not published.
- Added 42 company-aligned practice questions with recommended solutions, two alternatives and trade-offs.
- Added official feed configuration and a scheduled refresh workflow that writes to the same review branch only.

### Recruiter register
- `data/recruiters.csv` is intentionally header-only until named talent-acquisition professionals can be verified from public professional sources. Do not fill it with guessed names or private contact details.
