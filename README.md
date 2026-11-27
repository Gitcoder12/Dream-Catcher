# Dream-Catcher

A simple tracker of companies I want to work for.

I use it to research companies, follow their public work, find official career pages, prepare for interviews, and connect my public projects to the skills they may need.

## What is here

- [Companies](companies.md) — target companies and their technical areas.
- [Company fit dossiers](company-fit.md) — role-family fit, matching public projects, evidence strength and skill gaps for Mistral AI, Cerebras, Groq and OpenRouter.
- [Recent updates](data/updates.csv) — public company news with source links.
- [Update sources](data/feeds.csv) — official company feeds and manual source pages.
- [Interview practice](data/interviews.csv) — core and hard questions with solutions and alternatives.
- [Public repositories](data/repos.csv) — public repository details and archive status.
- [Careers](data/careers.csv) — official hiring pages.
- [People](data/people.csv) — public leaders and credited project contributors.
- [Recruiters](data/recruiters.csv) — named recruiters only when verified.
- [Project fit](repo-fit.md) — cross-company mapping between active public projects and company work.

## Data

The current research snapshot covers:

- 25 target companies
- 42 original interview practice questions across 21 companies
- 46 active public repository targets
- 48 public repositories in the inventory, including 2 archived repositories
- 23 sourced company updates before the first automatic feed refresh
- 22 companies with a verified official careers or open-positions route; 3 entries remain homepage-only pending verification

Private repositories are not listed here. They remain private and are not changed by this project. Archived public repositories are kept in the inventory but are not treated as active portfolio targets.

The interview questions are original company-aligned practice prompts. They are not claimed to be actual or favourite questions used by these companies. Each problem includes a recommended solution, two alternatives, trade-offs, edge cases and follow-ups.

## Updates

The refresh script updates public repository metadata and reads configured official company RSS/Atom feeds. New feed items are marked for review and their original links are kept. Companies without a verified feed remain on the manual source list; the updater does not invent updates.

The scheduled GitHub Actions workflow runs daily after it is enabled on the default branch. Eleven official RSS/Atom feeds are enabled; the remaining company pages are checked manually until a reliable feed is confirmed. It writes only to the existing review branch, never to `main`.

## Accuracy rules

- Keep a source link for every company update.
- Do not invent jobs, people, contact details or company relationships.
- A careers page does not mean a job is open.
- A project match is a research idea, not an endorsement or hiring signal.
- Do not publish private repository names or details.
- Distinguish direct project evidence from adjacent transferable skills and explicit gaps.
- Re-check vacancy status, location, seniority and eligibility on the employer's official page before applying.

---

## Engineering Audit & Handover — 2026-11-17

**Reviewed commit:** `57f7b62c50d616a079424a2cd762d75a71fa6102` (`main`). Static inspection covered `scripts/refresh.py`, source CSV structure, and README workflow claims; runtime refresh was not executed.

### Confirmed findings
- The refresh script imports public repository metadata and configured RSS/Atom items; feed entries retain source links and are marked for human review, consistent with the README's accuracy rules.
- The README states that scheduled updates write only to an existing review branch and never to `main`. This branch restriction is an important safety invariant; preserve it.
- The reviewed tree contains no automated test suite for feed parsing, metadata refresh, or CSV round-tripping.
- The README's snapshot counts are time-dependent and should be regenerated from the current CSV files rather than treated as permanent totals.

### Next actions
1. Add fixture-based tests for RSS/Atom parsing, malformed feeds, date handling, duplicate IDs, and failed sources.
2. Verify the scheduled workflow's target branch and permissions before enabling or changing its schedule.
3. Reconcile README counts from the CSV data in the same refresh process and keep every imported update in human-review status.

**Verification status:** static source/data inspection only; scheduled workflow, live feed imports, and tests remain unverified.

---

## Examples Used
- Tracking a target company's official career page
- Reviewing a sourced company update before adding it to the feed
- Mapping a portfolio project to a role's published technical requirements

---

## Comparison with Existing Open-Source Projects and Resources

Dream-Catcher is documented as a personal company-research and job-preparation tracker combining target companies, official careers routes, sourced updates, interview practice and project-fit notes. These resources provide adjacent job-discovery and interview-preparation references.

| Project / resource | Established focus | Relationship to Dream-Catcher |
|---|---|---|
| [Simplify New Grad Positions](https://github.com/SimplifyJobs/New-Grad-Positions) | Community-maintained list of early-career job opportunities | A job-listing resource; Dream-Catcher's distinction is maintaining a personal company dossier and linking company research to projects and interview preparation. |
| [The Tech Interview Handbook](https://github.com/yangshun/tech-interview-handbook) | Curated technical interview preparation material | A broad interview-learning resource; Dream-Catcher's interview prompts are organized around selected target companies and their technical context. |
| [GitHub Search](https://github.com/cli/cli) | Command-line access to GitHub search and repository workflows | A developer research tool rather than a career tracker; Dream-Catcher uses public repository metadata as one input to project-fit research. |

### Where Dream-Catcher is different
- **Company-centred workspace:** company updates, official careers routes, interview prompts, public repositories and project-fit notes are grouped by target employer.
- **Sourced research snapshot:** the README describes keeping source URLs and treating new feed items as review-needed rather than automatically verified.
- **Project-to-role mapping:** the intended workflow connects public portfolio work with a company's public technical areas as a research hypothesis, not a hiring prediction.

### Where established resources are stronger
Job lists and interview handbooks have broader community contributions and content depth. Dream-Catcher's advantage is personal organization and traceability, not job-market coverage or guaranteed hiring relevance.

### Evidence and privacy requirements
Keep company updates linked to official or clearly attributed sources, label feed items for human review, and never infer that a job is open from a careers page alone. Do not invent recruiter identities or publish private repository information. Project-fit notes are hypotheses, not endorsements or evidence of employer interest. This is a workflow comparison, not a job-placement benchmark.

---

## Repository navigation

[Alphabetical file index](FILE_INDEX.md)
