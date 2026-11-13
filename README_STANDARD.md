# README Standard: One Project, Two Levels of Understanding

Every repository README must help two readers without splitting the project into two conflicting stories:

1. A curious beginner who wants to know what the project does, why it matters and how to try it.
2. A serious engineer or researcher who wants to assess the problem definition, implementation, assumptions, evaluation, limitations and contribution path.

## Required order

1. **One-sentence purpose:** name the user/problem and outcome using ordinary language.
2. **Plain-language explanation:** use a concrete example. Define unavoidable technical terms the first time they appear.
3. **What works today:** list only capabilities present in the default branch and runnable with documented setup.
4. **Quick start:** prerequisites, exact commands, expected output and cleanup steps.
5. **Technical/research view:** problem framing, architecture, inputs, transformations/algorithms, outputs, dependencies, data sources and assumptions.
6. **Validation and evidence:** tests, benchmarks, dataset provenance, random seeds, hardware/software environment and result links.
7. **Limitations and safety:** identify mock data, simulations, heuristics, unsupported use, privacy/licensing boundaries and unvalidated claims.
8. **Contributing:** link CONTRIBUTING.md, FEATURE_UPGRADE_PLAN.md, and open issues with clear ownership/acceptance criteria.
9. **Engineering history:** link ACTIVITY_LOG.md and COMPANY_FIT.md.

## Editorial rule

Do not remove technical depth to make the README easier. Layer the explanation: simple first, technical detail next. Avoid marketing claims such as “production-ready”, “real-time”, “accurate”, “autonomous”, “safe” or “state of the art” unless the implementation and evidence support them.

## Collaboration contract

Each contribution should be a small work package with an issue, owner, acceptance criteria, test/evaluation method and evidence. Contributions should add or update tests and docs, report failures honestly and never commit secrets or private data.

## Special repository classes

- **Concept-stage projects:** say clearly that there is no runnable product yet. The first milestone is a scoped vertical slice, not a long feature list.
- **Research prototypes:** describe the hypothesis, baseline, dataset, metrics, uncertainties and reproducibility procedure.
- **Upstream mirrors/forks:** preserve upstream README, license and authorship. Add local notes in a clearly separated section and disclose divergence.
- **Archived projects:** label archived/read-only; do not present stale capabilities as maintained services.
- **Safety-sensitive projects:** clearly state that a prototype is not a clinical, emergency, security or engineering certification system.

## Per-repository copy-in draft

Each repository folder in the operating pack contains README_ADDENDUM_DRAFT.md with a project-specific beginner explanation and technical framing. Review it against the code before merging it into the root README.
