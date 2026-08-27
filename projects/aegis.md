# AEGIS

> Highest-priority project. Architecture is locked — see the change policy at the bottom before altering it.

| Field | Value | Status |
|---|---|---|
| Type | Team project | `VERIFIED` |
| Team size | 3 | `VERIFIED` |
| Shabaz's role | Team lead / original idea | `VERIFIED` |
| Lifecycle | `PLANNED` (architecture/design stage; code not started) | — |
| Expected completion | ~2 months from the current planning point | `PLANNED` |
| Hardware | Not finalized | `TO_VERIFY` |

## Status honesty

AEGIS is **planned / in progress at the design stage**. Do not write "Completed", "Production-ready", "Deployed", or "Successfully implemented" until Shabaz confirms completion. Mark it `PLANNED` (or `IN_PROGRESS` for design work) based on actual repository/code evidence at the time of writing. It is intended to become the **flagship** project once genuinely completed (expected ~2 months from the planning point). When a resume needs a completed project and AEGIS is still planned, use a completed project instead.

Leadership note: Shabaz is the originator and lead of this project, but AEGIS is **not** listed under the Leadership section of the profile (see [`../leadership/leadership.md`](../leadership/leadership.md)). That is deliberate.

## Concept

AEGIS is a planned AI-assisted emergency-response platform. A citizen reports an incident; the platform analyses the inputs and recommends a response; a human dispatcher verifies before resources are assigned; the incident is tracked to resolution and recorded for later analysis.

## Baseline architecture (locked)

```
Emergency
 → Citizen/Victim
 → SOS / Incident Report
 → GPS / Camera / Audio inputs
 → AEGIS Platform
 → AI Intelligence
 → Incident Type / Severity / Risk Factors
 → AI Recommendation
 → Human Dispatcher Verification
 → Resource Selection
 → Live Tracking
 → Responder
 → Incident Resolution
 → Digital Case / Evidence / Timeline / Analytics
 → Post-Incident Analysis
```

## Responsibility model (ownership boundary — preserve exactly)

- **AI:** Sense → Analyze → Recommend
- **Human:** Review → Decide → Dispatch
- **AEGIS:** Record → Track → Learn

AI does **not** independently control emergency response. Human dispatcher verification is part of the baseline. Workflows such as ambulance, police, admin, and a possible toll-plaza flow are planned design concepts, not built features.

## Architecture change policy

Do not alter the baseline or the AI-recommends / human-decides boundary without an explicit `ARCHITECTURE CHANGE PROPOSED` section (current architecture, proposed change, reason, technical impact, affected documents, approval status). A proposal is not the baseline until Shabaz approves it.
