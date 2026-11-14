# AI Worknotes — Dream-Catcher

**Maintainer:** Dharavath Satvik  
**Last updated:** 2026-11-14  
**Status:** Active refactor — one canonical draft PR

## Purpose

Dream-Catcher is a personal career-intelligence workspace. It tracks target employers, public company work, official hiring channels, publicly credited professional leaders/recruiting contacts, role families and evidence-backed portfolio fit.

It is a research aid, not an applicant-tracking system, employee database, endorsement record or claim of company relationships.

## Canonical file map

| Path | Single responsibility | Source of truth |
|---|---|---|
| `COMPANY_DIRECTORY.md` | Human-readable overview of target companies and their official entry points | `data/companies.csv` |
| `data/companies.csv` | One canonical row per employer/company group | Company identity and official URLs |
| `data/company_updates.csv` | Dated, source-linked public company announcements | Official company newsroom/blog |
| `data/public_people.csv` | Publicly documented leadership, project authors and explicitly public recruiting contacts | Official bios, public project credits or official hiring pages |
| `data/recruiting_channels.csv` | Official careers portals and public recruiting channels | Company-owned careers pages |
| `REPOSITORY_TARGET_MATRIX.md` | Provisional portfolio skills-fit mapping | Exact repository links; validate code before applications |
| `AI-WORKNOTES.md` | AI decisions, work log, limitations and next actions | Append dated entries here |

## No duplicate-document policy

- Do not recreate `COMPANY_INDEX.md`, `COMPANY_FIT.md`, `OPPORTUNITY_MAP.md` or a second `COMPANY_INTELLIGENCE.md`. Their useful scope is consolidated into the canonical files above.
- Do not put AI-generated sections, status notes or navigation lists in `README.md`.
- Do not maintain a second company list in prose when the canonical CSV already contains the records.
- Add updates as rows to `data/company_updates.csv`; do not create a new weekly/monthly file for every refresh.
- Add public recruiting contacts to `data/public_people.csv` only when their recruiting role and public source are explicitly verified. General careers portals belong in `data/recruiting_channels.csv`.

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

- The default branch contains a short original README plus portfolio-wide audit notes that are not specific to Dream-Catcher.
- Two draft PRs existed: PR #1 contained a broad 16-file documentation rollout; PR #2 contained a smaller overlapping company list.
- This refactor uses PR #2's branch as the single working branch and consolidates the company/recruiter/update data into one structure.
- X/LinkedIn follow lists are out of scope. Latest public company updates are included when an official source and date are available.
- No recruiter identities have been invented. The recruiting-channel file records official application routes; `data/recruiters.csv` is the dedicated recruiter register and currently contains only its schema because no individual recruiter record has yet been verified from an official/public professional source.
- The original README text is restored without AI notes.

## Work log

### 2026-11-14 — Canonical consolidation
- Replaced the overlapping company-index/intelligence/fit documents with one company directory and one canonical company CSV.
- Added a dated public updates feed, public people register and official recruiting-channel register.
- Kept the 61-row repository-fit matrix as a provisional mapping, not a functionality certification.
- Moved AI-maintained notes into this file and removed the AI addendum from README.
- Closed the duplicate documentation PR after preserving the relevant company/repository research in the canonical structure.
- Validation performed: source/link spot-checks and structural CSV review. No application build or runtime tests apply to this documentation/data-only change.

### Recruiter register
- `data/recruiters.csv` is intentionally header-only until named talent-acquisition professionals can be verified from public professional sources. Do not fill it with guessed names or private contact details.
