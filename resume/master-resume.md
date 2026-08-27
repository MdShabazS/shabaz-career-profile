# Master Resume — Mohammed Shabaz S

Single source of truth for resume content. Derive role/JD versions from this by changing emphasis only (see [`resume-strategy.md`](resume-strategy.md)). This is Markdown source, not a formatted PDF. Everything below is verified against the canonical files.

---

```markdown
# Mohammed Shabaz S

Software Developer | Embedded Engineer
Ballari, Karnataka, India
[md.shabaz.2005@gmail.com](mailto:md.shabaz.2005@gmail.com) · +91 79755 12403 · [LinkedIn](https://www.linkedin.com/in/shabaz17/) · [GitHub](https://github.com/MdShabazS) · Portfolio (link to be added)

## Summary

Final-year Electronics and Communication Engineering student (CGPA 8.38, graduating 2027) working across software and embedded systems. Currently a Student Intern at Nokia; earlier built and tested Android app-side features during an internship at iHelp Robotics, and built embedded firmware projects on microcontrollers. Comfortable with C, C++, Python, Java and SQL at a foundational level, and deepening data structures, algorithms and core CS for software and embedded roles.

## Education

Ballari Institute of Technology and Management (BITM), Ballari, Karnataka
B.E. Electronics & Communication Engineering — Final Year — Expected 2027 — CGPA 8.38
Class 12: 80% · Class 10: 86.88%

## Skills

Languages: C, C++, Python, Java, SQL
Software & Tools: Android Studio, OpenCV, Firebase, Git, GitHub
Embedded: Embedded C, Microcontrollers
CS Fundamentals: Data Structures & Algorithms (DSA), DBMS, Operating Systems, Computer Networks

## Experience

Nokia Solutions and Networks India — Student Intern — Bangalore
Sep 2026 – Present
- Student intern; project domain confidential.

iHelp Robotics Private Limited — AI Research Intern – Deep Learning & Model Development — Remote (Bangalore)
Mar 2026 – Aug 2026 · Project: MITRA
- Improved WiFi/RTSP live-stream handling in the MITRA Android app: reduced stream search delay, remembered the last working transport, and added refresh/stall recovery.
- Added a visual-freeze watchdog that reconnects when frame counters advance but the image stays visually stuck, plus on-screen stream-status and cloud-status panels and a guard that sends frames only when the cloud WebSocket is connected.
- Hardened offline voice commands (offline-preferred speech recognition with model recovery and microphone retry backoff) and verified behaviour across devices with logs, lint, and Gradle build checks.

IEEE EMBS Pune Section — Student Intern (Skin Disease Classification) — Online
Jun 2026 (1 month)
- Built a demo-level skin-disease image classifier in a 3-member team: model selection, training, evaluation, image processing, UI, and testing in Python.

## Projects

VisionPay — Real-time Indian currency detection (individual) ([repo](https://github.com/MdShabazS/visionpay))
- Built an offline currency-denomination detector with spoken feedback for visually impaired users: MobileNetV2 trained and converted to TensorFlow Lite, webcam inference, TTS.
- Collected ~400 images per denomination; added confidence/margin gating, temporal smoothing, a background class, and auto-count mode; reported ~93% validation accuracy.

Automotive Body Control Module — ESP32, Embedded C (individual) ([repo](https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32))
- Built an ESP32 body-control-module prototype with an OFF/ACC/ON ignition state machine, indicators, synchronized hazard mode, and an OLED dashboard.
- Structured the firmware with non-blocking millis-based scheduling, brake debouncing, GPIO abstraction, and edge-triggered serial logging.

AEGIS — AI-assisted emergency-response platform (team project, design stage — Planned/In Progress)
- Original idea and lead for a 3-member project designing an emergency-response platform.
- Defined a 15-stage incident workflow and a responsibility model where AI recommends and a human dispatcher verifies before resources are assigned.

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

- Main resume project pool: **VisionPay, Automotive BCM, AEGIS**. AEGIS is shown as a design-stage (Planned/In Progress) team project — if a company wants only completed work, drop AEGIS and promote MITRA or Smart Wellness Desk Assistant.
- For a software/Android version, add MITRA prominently and lead with VisionPay + MITRA.
- For an embedded version, lead with Automotive BCM and add Smart Wellness Desk Assistant (label it a team project).
- Skin Disease Classification is portfolio-first — include on a resume only when the role benefits from the healthcare/AI angle.
- Skills section uses "Microcontrollers"; specific boards (ESP32, STM32) appear only inside project bullets as that project's stack.
- Phone is included because a master resume is submitted directly by Shabaz; omit it from any public web copy.
- Nokia is shown as "Sep 2026 – Present"; keep the project/domain confidential.
- Certifications 1–2 have no issuer/date yet — quote them by name only until Shabaz provides details.
