# Shabaz Career Profile

> Shabaz's private career intelligence repository and single source of truth.

This repository stores structured professional facts for Mohammed Shabaz S. It is designed for long-term maintenance and safe AI use across resumes, interview preparation, company-specific placement planning, project explanation, and career decisions.

This is not a normal resume repository. It is a career knowledge base.

## Start Here

AI systems should read [`AI_CONTEXT.md`](AI_CONTEXT.md) first, then inspect the relevant canonical YAML or project files before generating any output. For projects, `facts.yaml` files are the canonical structured data; project `README.md` files are human-readable explanations.

## Repository Map

| Path | Purpose |
|---|---|
| `profile/` | Identity-safe personal context, education, languages, career goals |
| `skills/` | Programming levels, fundamentals state, hands-on technologies, proficiency rules |
| `projects/` | Canonical project facts, ownership boundaries, resume safety notes |
| `experience/` | Internship and program context |
| `leadership/` | Leadership roles and memberships |
| `memberships/` | Professional memberships |
| `certifications/` | Completed vs planned certifications and courses |
| `achievements/` | Selections and recognitions |
| `placement/` | BITM placement strategy and company-specific preparation workflow |
| `healthcare-research/` | Active healthcare research initiative, intentionally problem-agnostic for now |
| `resume/` | Resume-generation rules, safety constraints, and reusable master resume |
| `docs/` | Governance, schema, status, AI usage, changelog |
| `scripts/` | Repository validation utilities |

## Fact Status System

| Status | Meaning | Resume use |
|---|---|---|
| `VERIFIED` | Supplied by Shabaz or supported by provided evidence | Allowed |
| `PLANNED` | Intended future work, not completed | Do not present as completed |
| `TO_VERIFY` | Mentioned but insufficiently confirmed | Do not use as a strong claim |
| `EXCLUDED` | Explicitly excluded from primary profile/resumes | Do not use unless explicitly authorized |

Never convert `PLANNED`, `TO_VERIFY`, or `EXCLUDED` facts into verified resume claims without explicit user confirmation.

`fact_status` describes whether a fact is confirmed. `lifecycle_status` describes a project's current/completed state. `evidence_status` describes whether supporting artifacts are attached. Missing attached evidence does not downgrade a user-confirmed fact.

## Project Priority

Use this exact portfolio priority unless Shabaz explicitly changes it:

1. AEGIS — Team Lead / original idea
2. MITRA — Internship
3. Skin Disease Classification — IEEE Pune internship
4. NexCast Pro — Internship
5. VisionPay — Personal / individual project
6. Automotive BCM — Personal / individual project
7. Smart Wellness Desk Assistant — College team project

NIDAR and the undocumented hackathon project are excluded from the primary professional profile. See [`projects/EXCLUDED.md`](projects/EXCLUDED.md).

## Career Direction

Primary target roles:

- Software Engineer / Software Developer
- Embedded Engineer

For BITM placement preparation, software placement preparation receives higher priority because more software companies are expected to visit. Embedded remains an active parallel opportunity. AI/ML is currently an exploration area with project-level exposure, not a finalized specialization.

## AI Usage

AI assistants must:

- treat this repository as factual memory, not creative source material;
- treat project `facts.yaml` files as canonical structured project facts;
- use verified facts and preserve ownership boundaries;
- avoid inventing metrics, technologies, responsibilities, dates, titles, certifications, awards, or deployment claims;
- keep planned items visibly planned;
- keep excluded items out of resumes and primary professional profiles;
- keep AEGIS's human-dispatcher verification model intact.

## Update Rules

When adding new information:

1. Update the smallest canonical file that owns the fact.
2. Add or preserve `status`.
3. Keep team, internship, individual, and leadership ownership separate.
4. Document uncertainty with `TO_VERIFY`, `UNKNOWN`, or `NOT_PROVIDED`.
5. Run validation before committing.

Privacy reminder: never store passwords, API keys, tokens, government IDs, bank details, or other sensitive secrets in this repository.
