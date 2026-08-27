# Master Resume — Mohammed Shabaz S

Single source of truth for resume content. The PDF/DOCX in this folder are generated from exactly this content by [`../scripts/build_resume.py`](../scripts/build_resume.py) and validated by [`../scripts/ats_check.py`](../scripts/ats_check.py). Derive role versions by changing emphasis only (see [`resume-strategy.md`](resume-strategy.md) and [`ats-analysis.md`](ats-analysis.md)). Everything is verified against [`../PROFILE.md`](../PROFILE.md).

---

```
MOHAMMED SHABAZ S
Software Developer | Embedded Engineer
Ballari, Karnataka, India | 7975512403 | md.shabaz.2005@gmail.com |
linkedin.com/in/shabaz17 | github.com/MdShabazS | Portfolio: available on request

SUMMARY
Final-year Electronics & Communication Engineering student (CGPA 8.38) working across
application software and embedded firmware. Internship experience at Nokia and iHelp
Robotics, with projects in Android, computer vision, and microcontrollers using C/C++,
Python, and Embedded C.

EDUCATION
Ballari Institute of Technology and Management (BITM) — Ballari, Karnataka
B.E. Electronics & Communication Engineering | Final Year | Expected 2027 | CGPA 8.38
Class 12: 80% | Class 10: 86.88%

SKILLS
Languages: C, C++, Python, Java, SQL
Software & Tools: Android Studio, OpenCV, Firebase, Git, GitHub
Embedded: Embedded C, Microcontrollers
CS Fundamentals: Data Structures & Algorithms, DBMS, Operating Systems, Computer Networks

EXPERIENCE
Nokia Solutions and Networks India — Student Intern | Bangalore | Sep 2026 – Present
- Student intern contributing to engineering work; project scope is covered by company
  confidentiality.

iHelp Robotics Private Limited — AI Research Intern, Deep Learning & Model Development
Remote | Mar 2026 – Aug 2026 | Project: MITRA
- Improved live camera-stream reliability in the MITRA assistive Android app: reduced
  WiFi/RTSP stream search delay, persisted the last working transport, and added
  refresh/stall recovery.
- Built a visual-freeze watchdog that reconnects when frame counters advance but the
  image stalls; added on-screen stream- and cloud-status panels and a guard that sends
  frames only when the cloud WebSocket is connected.
- Hardened offline voice commands (offline-preferred speech recognition with model
  recovery and microphone retry backoff); verified builds across devices with Gradle
  test/lint/assemble runs and captured logs. Backend and model work were handled by
  another team.

IEEE EMBS Pune Section — Student Intern, Skin Disease Classification | Remote | Jun 2026
- Built a demo-level skin-disease image classifier with a 3-person team: model
  selection, training, evaluation, image processing, UI, and testing in Python.

PROJECTS
VisionPay — Individual | Python, MobileNetV2, TensorFlow Lite, OpenCV | github.com/MdShabazS/visionpay
- Built an offline Indian-currency recognizer with spoken feedback for low-vision users:
  trained a MobileNetV2 model, converted it to TensorFlow Lite, and ran real-time webcam
  inference with text-to-speech.
- Collected ~400 images per denomination across 6 note classes; added confidence/margin
  gating, temporal smoothing, a background class, and auto-count mode; reported ~93%
  validation accuracy.

Automotive Body Control Module — Individual | ESP32, Embedded C | github.com/MdShabazS/Automotive-Body-Control-Module-ESP32
- Built an ESP32 body-control-module prototype with an OFF/ACC/ON ignition state machine,
  indicators, synchronized hazard mode, and an OLED dashboard.
- Structured the firmware around non-blocking millis()-based scheduling with brake
  debouncing, GPIO abstraction, and edge-triggered serial logging.

AEGIS — Team (lead), design stage / in progress
- Leading a 3-person team designing AEGIS, an AI-assisted emergency-response platform:
  defined a 15-stage incident workflow where AI analyzes and recommends and a human
  dispatcher verifies before resources are dispatched.

LEADERSHIP & ACTIVITIES
- Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM (previously Treasurer)
- Treasurer, BITM Robotics Club
- Google Student Ambassador, 2025
- Selected Participant, IEEE SPACE 2026 — B.Tech Initiative

CERTIFICATIONS
Embedded Systems — Internshala Trainings (2025) | Python Programming — EISystems (2024) |
Google Cloud Generative AI — SmartBridge/SmartInternz (2025) | SQL for Data Analytics
with AI | Programming in C and C++ with AI

LANGUAGES
English, Kannada, Hindi, Urdu
```

---

## Notes

- **Links:** the header renders Email, LinkedIn, GitHub as clickable hyperlinks in the PDF/DOCX. Portfolio has no URL yet, so it shows "available on request" (no fabricated link) — swap in the real URL once deployed.
- **Skills vs bullets:** the Skills section follows the locked spec (Microcontrollers, not individual boards; no unheld protocols/RTOS). Specific platforms Shabaz actually used (ESP32, STM32, I2C, TensorFlow Lite, RTSP, etc.) appear only in project/experience bullets as that work's real stack.
- **Project pool:** master shows VisionPay, Automotive BCM, AEGIS (plus MITRA under Experience). For software/Android roles, emphasize MITRA + VisionPay; for embedded, lead with Automotive BCM + Smart Wellness Desk Assistant (team project); Skin Disease Classification stays portfolio-first.
- **AEGIS** is always shown as design-stage / in progress — never completed.
- **Phone** is included because Shabaz submits this master directly; omit it from public web copy.
- Regenerate the PDF/DOCX after any edit: `python3 scripts/build_resume.py`, then `python3 scripts/ats_check.py`.
