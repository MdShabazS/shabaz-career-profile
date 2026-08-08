# Data Governance

## Status Labels

| Status | Meaning | Resume use |
|---|---|---|
| `VERIFIED` | Confirmed fact/evidence | Yes |
| `PLANNED` | Intended future work | No, unless explicitly framed as planned |
| `TO_VERIFY` | Mentioned but insufficiently verified | No strong claims |
| `EXCLUDED` | Explicitly excluded | No |

## Canonical Sources

- Identity and education: `profile/`
- Skills: `skills/`
- Project order: `projects/project-priority.yaml`
- Project facts: `projects/<project>/facts.yaml` as canonical structured data
- Certifications: `certifications/completed.yaml` and `certifications/planned.yaml`
- Placement workflow: `placement/strategy.md`
- Resume safety: `resume/instructions.md`
- Source/evidence map: `docs/SOURCE_INDEX.md`

## Status Field Model

- `fact_status` describes whether a fact is confirmed.
- `lifecycle_status` describes project or initiative state.
- `evidence_status` describes whether supporting evidence has been attached.
- Missing repository evidence must not downgrade a user-confirmed fact.

## Non-Invention Rule

If a claim cannot be supported by this repository or Shabaz's current prompt, do not manufacture it.

## Ownership Rule

Use precise ownership:

- `Individual` only when explicitly confirmed.
- `Team` when the project was team-based.
- For team projects, distinguish Shabaz's personal contribution from the overall project.
- For internships, distinguish Shabaz's scope from other teams' scope.

## Evidence Rule

When a claim is supported by a certificate, project README, or other evidence, preserve the evidence reference where available. Do not infer technical details from a project title alone.

## Sensitive Information

Never store passwords, API keys, tokens, private access credentials, personal ID numbers, bank details, or other secrets in this repository.
