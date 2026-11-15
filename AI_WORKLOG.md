# AI Worklog

## Assessment
- Date: 2026-11-15
- Branch: `audit/initial-assessment-2026-11-15`
- Recommendation: Maintain and improve
- Maturity: Data-backed research tracker with a working refresh script and scheduled review-branch workflow.

## Purpose and implemented scope
Dream-Catcher tracks public target companies, official careers routes, public repository metadata, interview-practice prompts, and sourced company updates.

Verified implementation:
- Structured CSV datasets under `data/` for companies, careers, feeds, interviews, people, recruiters, repositories, and updates.
- `scripts/refresh.py` fetches public GitHub repository metadata and configured RSS/Atom feeds.
- Imported feed entries retain source URLs and are marked `feed_imported_needs_review`.
- CSV writes use a temporary file followed by replacement.
- `.github/workflows/refresh.yml` runs a scheduled/manual refresh and pushes only to `research/social-company-import-foundation`.
- README accuracy rules distinguish research prompts from actual company interview questions and avoid claiming jobs are open without evidence.

## Architecture and health
The project is a lightweight Python standard-library data pipeline with CSV storage and GitHub Actions scheduling. It has useful source-provenance rules and human-review status fields. The inspected root tree contains no test directory or unit-test suite.

## Findings
### P2 — Feed parsing and refresh pipeline lack automated tests
There are no tests for RSS/Atom variants, malformed XML, missing publication dates, duplicate URLs, oversized responses, CSV schema drift, or partial provider failures. Add deterministic fixture-based tests before relying on daily imports.

### P2 — Response-size handling should be explicit
`fetch_bytes` reads up to 5,000,001 bytes but does not explicitly reject an oversized response. A truncated XML payload may fail parsing; record a clear size-limit status and test this behaviour.

### P2 — Public GitHub API rate limits need observable handling
Repository refresh uses the unauthenticated public API endpoint. Rate limiting and transient failures should be surfaced in the refresh status with a retry/backoff policy rather than appearing as an unexplained failed refresh.

### P2 — Scheduled write workflow needs ongoing branch/permission monitoring
The workflow has `contents: write` and pushes to a fixed research branch. This is intentionally narrower than pushing to `main`, but the branch must remain present and the workflow should continue to use least privilege and a reviewable diff.

### P3 — Date reproducibility
`TODAY = date.today()` uses the runner's local date. If the workflow's reporting date is intended to be UTC or a named business timezone, define that explicitly and test date boundaries.

## Checks and evidence
- Inspected README, root tree, CSV inventory, `scripts/refresh.py`, and `.github/workflows/refresh.yml`.
- Refresh workflow exists; no separate test/lint workflow was found in the inspected root tree.
- Local refresh execution and feed network calls: NOT RUN.
- Unit tests: NOT RUN; no test suite was found in the inspected tree.
- Current default-branch combined status query returned no status entries; this does not establish CI health.
- Independent model review: NOT PERFORMED.
- External source URL reachability and factual accuracy of every CSV record: NOT exhaustively checked.

## Next actions
1. Add parser and CSV pipeline tests with local fixtures.
2. Add explicit response-size rejection and feed-specific error status.
3. Add retry/backoff for transient network and API rate-limit responses.
4. Validate every imported update's source URL and retain review state.
5. Define the reporting timezone and test date rollover.
