# Master Resume — Mohammed Shabaz S

Single source of truth for resume content. Derive role/JD versions from this by changing emphasis only (see [`resume-strategy.md`](resume-strategy.md)). This is Markdown source, not a formatted PDF. Everything below is verified against the canonical files.

---

```markdown
# Mohammed Shabaz S

Software Developer | Embedded Engineer
Ballari, Karnataka, India
[md.shabaz.2005@gmail.com](mailto:md.shabaz.2005@gmail.com) · +91 79755 12403 · [LinkedIn](https://www.linkedin.com/in/shabaz17/) · [GitHub](https://github.com/MdShabazS) · Portfolio (link to be added)

## Summary

Electronics and Communication Engineering student (CGPA 8.38, graduating 2027) working across software and embedded systems. Built and tested Android app-side features during an internship at iHelp Robotics, and built embedded firmware projects on ESP32 and STM32. Comfortable with C, C++, Python, Java and SQL at a foundational level, and currently deepening data structures, algorithms and core CS for software and embedded roles.

## Education

Ballari Institute of Technology and Management (BITM), Ballari, Karnataka
B.E. Electronics & Communication Engineering — Expected 2027 — CGPA 8.38
Class 12: 80% · Class 10: 86.88%

## Skills

Languages: C, C++, Python, Java, SQL
Embedded: ESP32, STM32, Arduino, Raspberry Pi, Embedded C
Software & Tools: Android Studio, OpenCV, Firebase, Git, GitHub
CS Fundamentals: Data Structures & Algorithms (DSA), DBMS, Operating Systems, Computer Networks

## Experience

Nokia Solutions and Networks India — Student Intern — Bangalore
Sep 2026 – Aug 2027 (incoming)
- Incoming student intern; project domain to be confirmed.

iHelp Robotics Private Limited — AI Research Intern (Software / Android) — Remote (Bangalore)
Mar 2026 – Aug 2026
- Improved WiFi/RTSP live-stream handling in the MITRA Android app: reduced stream search delay, remembered the last working transport, and added refresh/stall recovery.
- Added a visual-freeze watchdog that reconnects when frame counters advance but the image stays visually stuck, plus on-screen stream-status and cloud-status panels and a guard that sends frames only when the cloud WebSocket is connected.
- Hardened offline voice commands (offline-preferred speech recognition with model recovery and microphone retry backoff) and verified behaviour across devices with logs, lint, and Gradle build checks.

IEEE EMBS Pune Section — Student Intern (Skin Disease Classification) — Online
Jun 2026 (1 month)
- Built a demo-level skin-disease image classifier in a 3-member team: model selection, training, evaluation, image processing, UI, and testing in Python.

## Projects

AEGIS — AI-Assisted Emergency Response Platform (team project, design stage)
- Original idea and team lead for a 3-member project designing an emergency-response platform.
- Defined a 15-stage incident workflow and a responsibility model where AI recommends and a human dispatcher verifies before resources are assigned.

Automotive Body Control Module — ESP32, Embedded C ([repo](https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32))
- Built an ESP32 body-control-module prototype with an OFF/ACC/ON ignition state machine, indicators, synchronized hazard mode, and an OLED dashboard.
- Structured the firmware with non-blocking millis-based scheduling, brake debouncing, GPIO abstraction, and edge-triggered serial logging.

MITRA — Assistive Android app (iHelp Robotics internship)
- Delivered app-side reliability work for a live camera-stream assistive product (stream handling, cloud/stream status UI, offline voice commands, multi-device testing). Backend and model work belonged to another team.

## Additional Projects

VisionPay — Real-time Indian currency detection ([repo](https://github.com/MdShabazS/visionpay)): MobileNetV2 + TensorFlow Lite, offline webcam inference with spoken feedback; ~400 self-collected images per denomination; reported ~93% validation accuracy.
NexCast Pro — Floor-plan projection system (individual): Python, Flask, OpenCV, Tesseract OCR; splits plans into 1–12 projector zones for multi-projector display.
Smart Wellness Desk Assistant — STM32 Nucleo-L476RG (college team): sensor interfacing, wiring, and testing for a presence/temperature feedback device.

## Leadership

- Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM (previously Treasurer).
- Treasurer, BITM Robotics Club.
- Google Student Ambassador, 2025.

## Activities

- Selected Participant, IEEE SPACE 2026 — B.Tech Initiative.
- Participant, Techzone Nationals 2K25 Hardware Hackathon.
- Workshop: Designing Embedded AI Systems with the STMicroelectronics AI Ecosystem (DigiToad × STMicroelectronics).

## Certifications

- Embedded Systems — Internshala Trainings (8-week), 2025.
- Google Cloud Generative AI Virtual Internship — SmartBridge / SmartInternz, 2025.
- Python Programming — EISystems, 2024.
- SQL for Data Analytics with AI · Programming in C and C++ with AI.

## Languages

English, Kannada, Hindi, Urdu
```

---

## Notes for whoever formats the PDF

- Default top-3 project order (AEGIS, Automotive BCM, MITRA) is used above; AEGIS is shown as a design-stage team project — if a company wants only completed work, drop AEGIS and promote VisionPay.
- For a software-first version, reorder projects to MITRA, VisionPay, NexCast Pro and move software skills to the front.
- For an embedded-first version, lead with Automotive BCM and Smart Wellness Desk Assistant.
- Phone is included because a master resume is submitted directly by Shabaz; omit it from any public web copy.
- Re-verify: CGPA (may change), current semester, exact leadership dates, and whether items 1–2 under Certifications have issuer/date confirmed before quoting them.
