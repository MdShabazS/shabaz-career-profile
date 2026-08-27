# NexCast Pro

| Field | Value | Status |
|---|---|---|
| Type | Individual project | `VERIFIED` |
| Ownership | Built alone by Shabaz | `VERIFIED` |
| Lifecycle | `COMPLETED` | — |

## Overview

An intelligent floor-plan projection system: it ingests floor plans, extracts useful measurements/features, divides a plan into projector zones, and renders those zones for a multi-projector display.

## Known stack (do not extend beyond this)

Python, Flask, OpenCV, Tesseract OCR, pdf2image / Poppler, pygame, HTML/CSS/vanilla JavaScript, REST APIs, JSON configuration.

## Known capabilities (do not invent more)

- PDF / image / DXF / DWG ingest
- Auto-crop
- Wall detection and door-related CV processing
- OCR for dimensions and room labels
- 1–12 projector zone layouts with per-zone display assignment
- 1920×1080 zone output via a pygame display subprocess
- Persisted configuration and a web UI

## Boundaries

- Individual project — do not attribute to a team.
- Do not invent additional capabilities or frameworks. (Earlier context sometimes labelled this an "internship project"; the current canonical framing is an individual project. If the internship context matters for a specific output, mark it `TO_VERIFY` rather than asserting it.)
