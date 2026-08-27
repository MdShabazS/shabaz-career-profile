# MITRA

> Company product from the iHelp Robotics internship — not a personal project. Keep public descriptions high-level ([`../governance/CONFIDENTIALITY.md`](../governance/CONFIDENTIALITY.md)).

| Field | Value | Status |
|---|---|---|
| Type | Internship project (iHelp Robotics Private Limited) | `VERIFIED` |
| Positioning | Software / Android Development | `VERIFIED` |
| Lifecycle | `COMPLETED` (Shabaz's internship contribution) | — |
| Ownership | Company product; Shabaz contributed app-side software | `VERIFIED` |

## Overview (high-level, shareable)

MITRA is an assistive product in which an Android phone receives a live camera stream from hardware over WiFi/RTSP, supports app-side interaction and guidance, and includes a phone-camera fallback. Shabaz worked on the **Android app side**: stream reliability, cloud/stream status handling, offline voice-command robustness, and testing.

## Shabaz's contribution

See the full confirmed list in [`../experience/ihelp-robotics.md`](../experience/ihelp-robotics.md). In summary: WiFi/RTSP stream handling and reliability (search-delay reduction, transport memory, refresh/stall handling, a visual-freeze watchdog), stream- and cloud-status panels, a cloud send-guard tied to WebSocket connectivity, offline-preferred speech recognition with recovery and retry backoff, and extensive multi-device testing with logs and build verification.

## Boundaries

- Do **not** claim Shabaz developed the entire MITRA system.
- Backend and AI/model development belonged to another team — do not claim them.
- Do **not** expose confidential internal implementation, tooling, or proprietary detail. Public wording stays at the level above.
- No public GitHub link for MITRA (company/ongoing-sensitive).
