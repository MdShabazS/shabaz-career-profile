# Status System

This repository is a career **source of truth**. Every non-obvious fact carries a status label so that any reader — Shabaz, a recruiter (indirectly, through generated outputs), or an AI system (Claude, ChatGPT, Codex) — can tell a confirmed fact from an intention, a plan, or an unverified claim.

Two independent axes are used: **fact confidence** and **lifecycle state**. Do not collapse them.

## Fact confidence

| Label | Meaning | Allowed in resume / public output? |
|---|---|---|
| `VERIFIED` | Confirmed by Shabaz or supported by attached evidence. | Yes. |
| `TO_VERIFY` | Stated somewhere but not yet confirmed or evidenced. | Only with hedging; never as a strong claim. |
| `CONFIDENTIAL` | Real but restricted by an agreement (e.g. Nokia IP/NDA). | No, unless Shabaz confirms it is public. |
| `EXCLUDED` | Deliberately kept out of the primary profile. | No, unless Shabaz re-authorizes. |

Evidence has its own note where relevant:

- `evidence: attached` — a certificate/document is in [`../evidence/`](../evidence/).
- `evidence: user-confirmed` — Shabaz stated it; no document attached. This does **not** downgrade a `VERIFIED` fact.
- `evidence: TO_VERIFY` — supporting document not yet located.

## Lifecycle state (for work, projects, programs)

| Label | Meaning |
|---|---|
| `COMPLETED` | Finished. |
| `IN_PROGRESS` | Actively underway now. |
| `UPCOMING` | Committed/accepted but not yet started. |
| `PLANNED` | Intended; not started and not committed. |
| `LEARNING` | A skill currently being learned. |
| `BASIC` | A skill held at a basic/foundational level. |

## Hard conversion bans

Never silently convert:

- `PLANNED` or `UPCOMING` → `COMPLETED`
- `LEARNING` or `BASIC` → advanced / expert
- internship → full-time employment
- team project → individual project
- estimated / reported metric → verified metric
- intended responsibility → actual responsibility
- `CONFIDENTIAL` → public
- `EXCLUDED` → included

## Conflict resolution order

When two sources disagree:

1. Prefer the latest explicit, user-confirmed information.
2. For formal dates/titles, prefer official documents/certificates.
3. If it cannot be resolved, keep the uncertainty and mark `TO_VERIFY`.

Never invent to fill a gap. Missing information is written as `Not yet known` or `TO_VERIFY`.
