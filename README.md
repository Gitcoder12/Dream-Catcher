# Dream-Catcher

A simple tracker of companies I want to work for.

I use it to research companies, follow their public work, find official career pages, prepare for interviews, and connect my public projects to the skills they may need.

## What is here

- [Companies](companies.md) — target companies and their technical areas.
- [Recent updates](data/updates.csv) — public company news with source links.
- [Update sources](data/feeds.csv) — official company feeds and manual source pages.
- [Interview practice](data/interviews.csv) — core and hard questions with solutions and alternatives.
- [Public repositories](data/repos.csv) — public repository details and archive status.
- [Careers](data/careers.csv) — official hiring pages.
- [People](data/people.csv) — public leaders and credited project contributors.
- [Recruiters](data/recruiters.csv) — named recruiters only when verified.
- [Project fit](repo-fit.md) — possible links between active public projects and company work.

## Data

The current research snapshot covers:

- 21 target companies
- 42 original interview practice questions across 21 companies
- 46 active public repository targets
- 48 public repositories in the inventory, including 2 archived repositories
- 23 sourced company updates before the first automatic feed refresh
- 21 official careers routes

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
