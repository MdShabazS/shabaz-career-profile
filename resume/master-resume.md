# Master Resume — Mohammed Shabaz S

Single source of truth for resume content. The PDF/DOCX in this folder are generated from this content by [`../scripts/build_resume.py`](../scripts/build_resume.py) and validated by [`../scripts/validate_resume.py`](../scripts/validate_resume.py). Design follows Shabaz's prior resume template (centered navy header, ruled sections, right-aligned dates); facts are current, verified against [`../PROFILE.md`](../PROFILE.md). Research: [`../research/TIER1_RESUME_RESEARCH.md`](../research/TIER1_RESUME_RESEARCH.md). Derive role versions by changing emphasis only ([`resume-strategy.md`](resume-strategy.md), [`ats-analysis.md`](ats-analysis.md)).

**Header:** name, `Software Developer | Embedded Engineer`, then `Ballari, Karnataka | +91 79755 12403 | <email, clickable> | [icon] LinkedIn | [icon] GitHub`. LinkedIn/GitHub are clickable labels (icons + word), not raw URLs; email is shown and clickable. No portfolio URL (not deployed).

---

```
MOHAMMED SHABAZ S
Software Developer | Embedded Engineer
Ballari, Karnataka | +91 79755 12403 | md.shabaz.2005@gmail.com | LinkedIn | GitHub

SUMMARY
Final-year Electronics & Communication Engineering student (CGPA 8.38) building across
software and embedded systems. Internships at Nokia and iHelp Robotics, with projects in
Android, computer vision, and microcontroller firmware using C, C++, Python and Embedded C.
Currently deepening data structures, algorithms and SQL for software and embedded roles.

TECHNICAL SKILLS
Languages: C, C++, Python, Java, SQL
Software & Tools: Android Studio, OpenCV, Firebase, Git, GitHub
Embedded: Embedded C, Microcontrollers
CS Fundamentals: Data Structures & Algorithms, DBMS, Operating Systems, Computer Networks

EXPERIENCE
Student Intern                                                        Sep 2026 – Present
Nokia Solutions and Networks India                                              Bangalore
- Working as a Student Intern at Nokia.

AI Research Intern – Deep Learning & Model Development                 Mar 2026 – Aug 2026
iHelp Robotics Private Limited · Project: MITRA                                     Remote
- Improved live camera-stream reliability in the MITRA assistive Android app across 2 video
  sources (hardware WiFi/RTSP and phone-camera fallback): cut stream search delay, persisted
  the last working transport, and added refresh/stall recovery.
- Engineered a visual-freeze watchdog plus 3 status/guard mechanisms — a stream-status panel,
  a cloud-status panel, and a WebSocket-gated send guard — and fixed a live-refresh loop that
  recurred after 5 minutes.
- Hardened offline voice commands (offline-preferred recognition with model recovery and
  microphone retry backoff) and verified builds across multiple devices with Gradle
  test/lint/assemble; delivered 6+ app-side improvements while model and backend stayed with
  a separate team.

Student Intern – Skin Disease Classification                                     Jun 2026
IEEE EMBS Pune Section                                                              Remote
- Trained and evaluated a skin-disease image classifier in a 3-member team during a 1-month
  IEEE EMBS internship — model selection, training, evaluation, and Python image-processing
  and testing; delivered a working demo-level workflow.

PROJECTS
VisionPay — Real-Time Indian Currency Detection                                    [GitHub]
Python, OpenCV, TensorFlow Lite, MobileNetV2, Text-to-Speech
- Developed an offline, real-time tool that recognizes Indian currency from a live webcam and
  speaks the result aloud for visually impaired users.
- Collected ~400 images per denomination across 6 classes (Rs.10–Rs.500) and trained a
  MobileNetV2 classifier converted to TensorFlow Lite, reporting ~93% validation accuracy.
- Improved reliability with 4 mechanisms: confidence/margin gating, temporal smoothing, a
  background class, and an auto-count mode.

Automotive Body Control Module                                                     [GitHub]
ESP32, Embedded C, GPIO, OLED, State Machine
- Programmed an ESP32 body-control module with a 3-state (OFF/ACC/ON) ignition FSM driving 6+
  functions: indicators, synchronized hazard, brake logic, buzzer and an OLED dashboard.
- Architected a non-blocking millis()-based scheduler with brake debouncing, GPIO abstraction
  and edge-triggered logging for predictable real-time behavior.

Smart Wellness Desk Assistant                                                      [GitHub]
STM32 Nucleo-L476RG, STM32 HAL, Embedded C, Sensors · College team project
- Interfaced 2 sensor types (ultrasonic presence and ADC temperature), an I2C OLED, timers and
  buzzer alerts on an STM32 Nucleo-L476RG as part of a college team; handled wiring, testing
  and debugging in STM32CubeIDE.

AEGIS — AI-Assisted Emergency Response Platform
Team lead · Architecture / design stage (in progress)
- Leading a 3-member team on an original concept, designing a 15-stage response architecture —
  from incident reporting and GPS/camera/audio inputs through AI analysis, human-dispatcher
  verification, resource dispatch and live tracking.

EDUCATION
B.E. Electronics & Communication Engineering                                  Expected 2027
Ballari Institute of Technology and Management (BITM), Ballari         Final Year · CGPA 8.38
Class 12: 80% · Class 10: 86.88%

LEADERSHIP & ACTIVITIES
- Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM (promoted from Treasurer); Treasurer,
  BITM Robotics Club.
- Google Student Ambassador (2025); Selected Participant, IEEE SPACE 2026 — B.Tech Initiative.

CERTIFICATIONS
Embedded Systems — Internshala Trainings (2025) · Python Programming — EISystems (2024) ·
Google Cloud Generative AI — SmartBridge/SmartInternz (2025) · SQL for Data Analytics with AI ·
Programming in C and C++ with AI

LANGUAGES
English · Kannada · Hindi · Urdu
```

---

## Notes

- **Links (PDF/DOCX):** email, LinkedIn, GitHub, and each project "GitHub" are live hyperlinks; LinkedIn/GitHub in the header are icon+label (no raw URLs). `[GitHub]` above marks where a right-aligned clickable link sits per project.
- **Skills vs bullets:** the Skills section follows the locked spec (Microcontrollers, not individual boards; no unheld protocols/RTOS). Specific platforms actually used (ESP32, STM32, I2C, TensorFlow Lite, MobileNetV2, RTSP) appear only in bullets.
- **Projects shown:** VisionPay, Automotive BCM, Smart Wellness Desk Assistant (team), AEGIS (in progress). MITRA sits under the iHelp experience; Skin Disease Classification under the IEEE EMBS experience. Skin Disease is otherwise portfolio-first.
- **Tailoring:** software/Android roles → lead VisionPay + MITRA; embedded roles → lead Automotive BCM + Smart Wellness. Never change facts between versions.
- **AEGIS** is always design-stage / in progress — never completed.
- Regenerate after edits: `python3 scripts/build_resume.py` then `python3 scripts/validate_resume.py`.
