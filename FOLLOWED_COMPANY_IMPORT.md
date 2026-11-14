# X and LinkedIn Company-Follow Import

**Maintainer:** Dharavath Satvik  
**Snapshot:** 2026-11-14  
**Status:** Waiting for account exports or user-provided source data.

## Access limitation

The connected account tools currently available to this workflow do not expose the user's X following list or LinkedIn followed-company pages. The LinkedIn lookup capability is for finding professional profiles; it does not provide a list of pages the user follows. Therefore, no company below is labelled as followed on either platform unless evidence is imported.

## What to provide

Upload the relevant account-export files from:

- **X:** the account archive file containing the accounts you follow. Company accounts will be separated from individual people and other account types.
- **LinkedIn:** the export data for followed companies/pages, if included in the archive. If the export does not include page follows, provide a page-follow export or screenshots/list copied from the account UI.

Do not provide passwords, session cookies, authentication tokens, private messages, or unrelated personal account data.

## Import procedure

1. Read the supplied export without changing the original.
2. Extract only public company, organisation, lab, startup and employer accounts/pages.
3. Separate individual people, creators, recruiters, universities, communities, products and news outlets into distinct categories; do not misclassify them as employers.
4. Resolve aliases and subsidiaries carefully. Keep Amazon and AWS linked as related entities but retain distinct records when the followed account is AWS.
5. Deduplicate using official domain and verified account/page URL, not display name alone.
6. Store platform evidence separately: x_followed, linkedin_followed, and evidence_source.
7. Preserve the source filename, export date and import date. Do not retain unrelated personal data.
8. Mark ambiguous accounts needs_review; do not guess.
9. Compare imported companies with the existing target list. Add newly discovered organisations without deleting existing research targets.
10. Produce a change summary with counts: imported accounts, confirmed company pages, duplicates, non-company accounts excluded and unresolved records.

## Data contract

The canonical table is [data/companies.csv](data/companies.csv). Keep these meanings:

- x_followed: true, false, or unknown; true/false requires export evidence.
- linkedin_followed: true, false, or unknown; true/false requires export evidence.
- follow_evidence: source filename and row/account identifier, not private credentials.
- verification_status: prior_research_target, confirmed_follow, needs_review, or unverified.
- source_checked_at: ISO date when the source was actually checked. Never backdate.

## Privacy and accuracy

Only process the company-follow data needed for Dream-Catcher. Do not ingest private messages, email addresses, phone numbers, personal profiles or unrelated contacts. Do not publish private account exports in the repository. The repository should contain only the minimal company-level records and public URLs required for the project.
