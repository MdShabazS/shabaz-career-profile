# Repository Schema

The repository separates human-readable Markdown from machine-readable YAML.

## Directory Contract

| Path | Contents |
|---|---|
| `README.md` | Public-facing overview, privacy-safe |
| `AI_CONTEXT.md` | First-read AI context and operating rules |
| `profile/` | Personal, education, career goals, languages |
| `skills/` | Programming, fundamentals, hands-on exposure, proficiency rules |
| `projects/` | Project READMEs, structured facts, exclusions, priority |
| `experience/` | Internship/program summaries and index |
| `leadership/` | Leadership roles |
| `memberships/` | Membership records |
| `certifications/` | Completed and planned certification records |
| `achievements/` | Selections and recognitions |
| `placement/` | BITM placement strategy |
| `roadmap/` | Learning progress and planned growth |
| `healthcare-research/` | Active healthcare research boundary |
| `resume/` | Resume-generation instructions |
| `docs/` | Governance, schema, status, changelog |
| `scripts/` | Validation scripts |

## YAML Conventions

Structured files should use:

- `schema_version`
- `status` or `fact_status` when the file records factual claims
- `PLANNED`, `TO_VERIFY`, `UNKNOWN`, or `NOT_PROVIDED` for incomplete facts
- explicit `boundary` or `resume_boundary` fields where overclaiming is likely

## Project File Convention

Each active project should include:

- `README.md` for human narrative
- `facts.yaml` for structured AI parsing

The two files must not contradict each other.
