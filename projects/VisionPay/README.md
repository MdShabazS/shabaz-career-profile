# VisionPay

VisionPay is a personal individual project. The canonical structured record is [`facts.yaml`](facts.yaml).

## Goal

Real-time Indian currency denomination detection with spoken feedback for visually impaired users.

## Confirmed Facts

- Personally collected approximately 400 images per denomination
- Denominations: ₹10, ₹20, ₹50, ₹100, ₹200, ₹500
- MobileNetV2
- TensorFlow Lite
- Real-time webcam inference
- Offline CPU-oriented inference
- TTS
- Confidence/margin gating
- Temporal/majority smoothing
- Background class
- Auto-count mode
- Reported validation accuracy around 93% according to the supplied project description

## Implementation Boundary

Training code was AI-assisted. Do not falsely claim that every line of training code was manually written by Shabaz.

## Not Completed

The following were roadmap items, not completed features unless new evidence is added:

- YOLO-based detector
- Counterfeit checks
- Hindi TTS
- Android/Raspberry Pi deployment
- Multi-note detection
