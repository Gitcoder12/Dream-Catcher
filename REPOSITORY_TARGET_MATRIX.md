# Repository-to-Company Target Matrix

**Maintainer:** Dharavath Satvik  
**Snapshot:** 2026-11-14  
**Status:** Recovered mappings from prior project-planning notes; not endorsements or evidence of adoption.

This matrix records where a repository's technical direction may demonstrate relevant skills. It does not claim that any company uses, sponsors, endorses, or has reviewed the project.

| Repository | Potential company targets | Skills / technical overlap to demonstrate | Evidence status |
|---|---|---|---|
| ARK | OpenAI; Anthropic; Google DeepMind; NVIDIA | AI safety evaluation, agent reliability, reward-hacking tests, runtime monitoring, simulation | Prior planning mapping; validate against current repo implementation |
| RepoForge | GitHub; OpenAI; Anthropic | Developer tooling, repository analysis, model orchestration, safe code-edit workflows | Prior planning mapping; validate against current repo implementation |
| Robo-Drafter | NVIDIA; Skild AI; Boston Dynamics; ABB | Robotics workflows, autonomy, simulation, controls and perception | Prior planning mapping; distinguish simulation from physical-robot evidence |
| TokenBurst | NVIDIA; Qualcomm; Hugging Face | Model inference, performance, edge deployment, model tooling | Prior planning mapping; validate against current repo implementation |
| Hardware-Box | ABB; Tata Elxsi; NVIDIA; Qualcomm | Hardware design, embedded systems, CAD/EDA workflows, engineering validation | Prior planning mapping; validate against current repo implementation |
| Ember | Tata Elxsi; TCS; AWS | Thermal/food-safety engineering, sensor data, applied ML, cloud deployment | Prior planning mapping; synthetic calibration is not real-world validation |

## Mapping policy

- Only add a mapping when a concrete repository capability can be demonstrated in code, tests, a reproducible experiment or a documented prototype.
- Keep **target fit** separate from **company follow evidence**.
- Keep **target fit** separate from **job availability** and **application status**.
- Cite the exact repository path, demo, test, paper or benchmark that supports each claimed skill.
- Do not claim a company-specific stack, team or hiring requirement without a current official source.
- Add a confidence label only when the reason is written down: strong, plausible, or weak.
- Revisit mappings when the repository changes materially or the company publishes new technical work.

## To expand

Other repositories should be added only after reviewing their current default-branch code and README. Do not infer fit from repository names alone.
