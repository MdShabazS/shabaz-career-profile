# iHelp Robotics — AI Research Intern (public positioning: Software / Android Development)

| Field | Value | Status |
|---|---|---|
| Company | iHelp Robotics Private Limited | `VERIFIED` |
| Official designation | AI Research Intern – Deep Learning & Model Development | `VERIFIED` (per offer letter) |
| Project | MITRA | `VERIFIED` |
| Period | 23 March 2026 – 23 August 2026 (~5 months) | `VERIFIED` |
| Work location | Bangalore | `VERIFIED` |
| Mode | Remote | `VERIFIED` |
| Lifecycle | `COMPLETED` | — |

## Positioning

Present this primarily as **Software Development / Android Development**, not as AI/ML. The official title on the offer letter is "AI Research Intern – Deep Learning & Model Development" and may be quoted as the formal designation, but the described contribution should lead with the app-side software and testing work Shabaz actually did. Backend and AI/model development belonged to another team — do not claim it.

Project detail lives in [`../projects/mitra.md`](../projects/mitra.md). MITRA is a company product; keep public descriptions high-level ([`../governance/CONFIDENTIALITY.md`](../governance/CONFIDENTIALITY.md)).

## Confirmed contribution (app-side)

**Android / MITRA app**
- Improved hardware WiFi and RTSP stream handling.
- Reduced hardware stream search delay.
- Added memory for the last successful stream transport.
- Added RTSP refresh / stall handling.
- Fixed a live-refresh looping issue that appeared after 5 minutes on one device.
- Added a visual-freeze watchdog that reconnects when frame counters advance but the image stays visually stuck.
- Added a stream-status panel to the left of the live feed.
- Added a cloud-status panel to the right of the live feed.
- Added a cloud guard so frames are prepared/sent only when the WebSocket is connected.

**Voice / commands**
- Investigated voice behaviour differences across devices.
- Identified offline speech-model issues on one device.
- Added an offline-preferred speech-recognition setup.
- Added recovery for a missing offline speech language/model.
- Added internet-based preparation for the offline speech model.
- Added microphone retry backoff.

**Testing**
- Tested hardware stream and voice behaviour across devices.
- Tested fresh install, stream, microphone, refresh, and command behaviour.
- Captured logs and test evidence.
- Verified builds with Gradle tests/lint/assemble multiple times.
- Compared hardware stream delay in a reference player versus the app; later testing did not reproduce a previously observed ~8-second delay.

## Boundaries

- Do **not** claim Shabaz built the entire MITRA system.
- Do **not** claim backend or AI/model development as Shabaz's work.
- Keep public wording high-level; do not expose company-confidential implementation detail.
