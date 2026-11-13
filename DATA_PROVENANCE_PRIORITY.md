# Data Provenance Priority Register

**Snapshot:** 2026-11-13  
**Purpose:** Direct independent reviewers toward repositories where data origin, real-vs-synthetic status, freshness or official attribution could materially affect public trust.

This register is a **review checklist**, not a finding that every listed dataset exists or is invalid. Except where explicitly stated, reviewers must inspect the current source tree before assuming a data path or feature exists.

## Highest priority

### Civicshield — P0
- Current README claims 114 venues, FSSAI verification counts, inspector audits, dish ratings and live FOSCOS verification. Those historical claims were preserved, but the authoritative evidence behind them has not been independently established.
- Inspect hotels.json and the browser-embedded venue records. Trace every venue name, FSSAI-shaped number, status, date, score, owner/phone field, inspector identity and dish rating to a primary public source or documented permission.
- A sequential-looking licence number or official label is not evidence of validity. Mark unverified records as unverified; do not replace them with Demo Venue placeholder rows.
- [PR #1](https://github.com/Gitcoder12/Civicshield/pull/1) is closed without merge and its worklog documents a synthetic placeholder substitution. Do not treat it as a valid replacement dataset.
- Check that citizen submissions cannot change trusted venue or inspection records and that official inspector workflows require authentication and auditable identity.

### Truthstream — P0/P1
- The default backend includes an in-memory/demo evidence retriever. Identify every fixed example, source name, credibility score, snippet and URL.
- An open PR #2 includes an example item named "Official Government Registry" with a null URL. This is illustrative content, not an actual government source. Keep it visibly labelled as mock/demo and never surface it as retrieved evidence.
- For live providers, preserve provider URL, retrieval timestamp, original title/snippet, provider identity and any transformations. External metadata retrieval does not prove that a source supports or contradicts a claim.
- Confidence scores must be described as model outputs, not factual truth probabilities, unless formally calibrated and externally validated.

## Public records, scraping and research metadata

### AP-Developer and Politrack — P1
- Confirm every scraped or user-provided item links to the original publisher/source and includes retrieval/publication timestamps.
- Separate reported allegations, media summaries, official statements and independently verified facts.
- Document source selection, deduplication, sentiment/party attribution rules, missing coverage and known bias. Do not present scraped mention counts as proof of wrongdoing or objective party performance.
- No fabricated political identities, incident records, quotes or official statements.

### Brightscope — P1
- Verify that OpenAlex/Crossref adapters return actual source records and preserve source IDs/URLs, authorship, publication metadata and retrieval timestamps.
- Deduplication must not merge distinct works or invent authors, affiliations, citations, abstracts or journal metadata.
- Clearly distinguish source-provided citation counts from estimates or derived metrics.

### Dream-Catcher — P1
- Every company project, executive title, team reference, job family and source link must be checked against official company/newsroom/research/careers pages.
- Use public professional information only. No private contact details, employee dossiers, personal data, confidential or classified material.
- A repository-to-company mapping is a prospective skills-fit hypothesis, never an adoption, customer, endorsement or partnership claim.

## Geospatial, public directory and emergency information

### DeepMap
- Trace coordinates, elevations, risk descriptions, access restrictions and landmark facts to public sources.
- Distinguish illustrative exploration difficulty and hazard heuristics from official safety assessments or route guidance.
- Include coordinate range checks, units, datum assumptions and source dates.

### RapidAid-Network
- Verify any emergency service, shelter, hospital, volunteer or supply location through authoritative sources.
- Store update time, geographic coverage, operational status and contact provenance. Stale data must be visibly marked.
- Do not invent emergency contacts, dispatch capacity or availability.

### Public-Space and Temple-List
- Verify names, addresses, coordinates, opening/access details and category labels from attributable sources or owner/community submissions.
- Distinguish public facts from user-submitted descriptions and keep a correction/reporting trail.
- Do not publish private residential details or sensitive security information.

### VoltZone
- Treat EV charging points, rental availability, power capacity, outage status and location records as unverified until source, timestamp and operational status are established.
- Do not imply a real charging network or active backup-power service if the repository is only a prototype.

### Hydro-Glance
- Preserve the provenance of any sensor, rainfall, river, groundwater or weather series.
- Record station/source ID, sensor type, units, sampling interval, calibration, missingness, timezone and collection period.
- Keep synthetic sensor series separate from field observations.

## Engineering and simulation data

### Ember
- The project README states calibration has been tested on synthetic measurements only. This validates code paths, not real-world thermal accuracy.
- Preserve real probe readings. Never replace them with generated measurements. Record probe model, food category, packaging, start/end temperature, time, ambient conditions, units, protocol, calibration and consent where applicable.
- Do not claim ML accuracy until tested on held-out real measurements and compared with calibrated physics baselines.

### Robo-Drafter
- The dashboard clarification in open PR #2 says the Streamlit dashboard uses synthetic illustrative fitness values and is not connected to a physical robot, camera, simulator or hardware controller.
- Keep the synthetic dashboard labelled. Do not present simulated fitness charts as physical-robot performance or experimental evidence.

### Data-Center-Planner
- Separate genetic-algorithm simulations and illustrative rack inputs from measured data-centre telemetry.
- Record rack, power, thermal, capacity and workload assumptions. Do not claim production PUE, energy savings or thermal optimisation without measured validation.

### Hardware-Box
- Preserve the source and revision of CAD/mesh/3MF/STL/BOM/KiCad inputs. Mark tutorial fixtures and test-corruption files as synthetic test artefacts.
- Units, tolerances, material specifications and statistical fit assumptions must be explicit. Tool output is not engineering certification.

### ARK
- Keep simulator observations, synthetic episodes, hand-authored labels, validation episodes and any real-world data distinctly labelled.
- Preserve random seeds, environment version, monitor configuration, model/policy identity and evaluation split.
- Do not claim general alignment or real-world safety from finite simulator tests or heuristic threat scores.

## Archive, forks and inherited datasets

### Repo-Vault
- Its README states that inventory is not backup completion and that no restore test had been performed at the time of the source snapshot.
- Distinguish repository inventory, copied Git objects, LFS/release assets, GitHub metadata, checksums and restore verification. Never claim a backup is complete without a successful restore test.
- Never put tokens, credentials, private keys, raw secrets or private personal data into manifests or archive logs.

### dspy, lm-evaluation-harness, vllm and ollama
- These are upstream forks. Preserve upstream licence/copyright/NOTICE files and benchmark/data attribution.
- Separate fork-only modifications from inherited upstream source. Do not claim upstream benchmark results or core functionality as original work.
- Check that copied datasets and benchmarks comply with upstream licences and redistribution conditions.

## Required classification

For every record or dataset classify as exactly one of:
- **Verified external data** — source and licence checked, provenance preserved.
- **Maintainer/user-provided data** — origin is documented by the maintainer/user; external truth not implied.
- **Synthetic test fixture** — generated solely for tests, clearly labelled and isolated.
- **Illustrative demo data** — visibly synthetic/fictional and never presented as real.
- **Scraped candidate** — retrieved from a source but not independently fact-checked.
- **Unknown/unverified** — preserve unchanged; no claim of authenticity.

Never silently promote data from one class to another. Record provenance and transformations at the field or record level where practical.
