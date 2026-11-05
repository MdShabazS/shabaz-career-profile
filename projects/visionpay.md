# VisionPay

| Field | Value | Status |
|---|---|---|
| Type | Individual project | `VERIFIED` |
| Lifecycle | `COMPLETED` | — |
| GitHub | https://github.com/MdShabazS/visionpay | `VERIFIED` |

## Overview

Real-time Indian currency-denomination detection with spoken feedback, aimed at visually impaired users. Offline, CPU-oriented inference.

## Dataset

Approximately 400 personally collected images per denomination across six classes: ₹10, ₹20, ₹50, ₹100, ₹200, and ₹500 (about 2,400 images total).

## Known stack

Python, MobileNetV2, TensorFlow Lite, OpenCV / webcam pipeline, TTS.

## Techniques

- Real-time webcam inference; offline CPU-oriented inference
- Confidence / margin gating
- Temporal / majority-vote smoothing
- Background class
- Auto-count mode

## Reported result

Reported **approximately 93% validation accuracy** — a reported project-description figure, not an independently verified benchmark. Do not restate it as a verified metric, and do not invent additional metrics.

## Boundaries

- Training code was AI-assisted; do not claim every line was hand-written.
- Not built (do not present as done): YOLO-based detector, counterfeit checks, Hindi TTS, Android/Raspberry Pi deployment, multi-note detection.
