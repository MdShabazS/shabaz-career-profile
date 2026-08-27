# Data Policy

How facts enter, live in, and leave this repository.

## Separation of concerns

Three kinds of content are kept distinct and must never be blurred into each other:

1. **Facts about Shabaz** — verified profile data. Lives in `profile/`, `experience/`, `projects/`, `skills/`, `certifications/`, `leadership/`, `professional-activities/`.
2. **External research** — market/role requirements gathered from outside sources. Lives in `research/`. It is never a source of Shabaz's credentials.
3. **Recommendations** — plans and gap analysis derived from 1 and 2. Lives in `skills/tier1-skills-roadmap.md`, `resume/`, `portfolio/`.

External research must never create a fact about Shabaz. A requirement that "Tier-1 roles expect RTOS" does not mean Shabaz knows RTOS.

## Ownership precision

- Use `Individual` only when Shabaz explicitly confirmed he worked alone.
- Use `Team` for team work, and state Shabaz's specific contribution separately from the team's output.
- For internships, separate Shabaz's scope from other teams' scope.
- Do not infer technical detail from a project title alone.

## Non-invention rule

If a claim cannot be supported by this repository or by Shabaz's explicit statement, do not manufacture it. Write `Not yet known` or `TO_VERIFY`.

Specifically, never invent: metrics, technologies, responsibilities, dates, titles, certifications, certificate issuers, awards, rankings, team sizes, deployment/production claims, or model architectures.

## Evidence

Attached proof documents live in [`../evidence/`](../evidence/) with an index. A `VERIFIED` fact confirmed by Shabaz stays `VERIFIED` even when no document is attached; only its `evidence` note reflects the missing artifact.

## Sensitive data

Never commit passwords, API keys, tokens, private access credentials, government ID numbers, bank details, offer-letter PDFs, or screenshots containing private data. See [`CONFIDENTIALITY.md`](CONFIDENTIALITY.md).
