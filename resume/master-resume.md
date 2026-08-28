# Master Resume — Mohammed Shabaz S

Single source of truth for resume content. The PDF/DOCX in this folder are generated from this content by [`../scripts/build_resume.py`](../scripts/build_resume.py) and validated by [`../scripts/validate_resume.py`](../scripts/validate_resume.py). Design follows Shabaz's prior resume template (centered navy header, ruled sections, right-aligned dates); facts are current and verified against [`../PROFILE.md`](../PROFILE.md). Research: [`../research/TIER1_RESUME_RESEARCH.md`](../research/TIER1_RESUME_RESEARCH.md). Strategy & ATS analysis: [`resume-strategy.md`](resume-strategy.md), [`ats-analysis.md`](ats-analysis.md).

**Primary target:** Embedded Engineer / Automotive Embedded Systems. **Secondary target:** Software Engineering. **Headline:** `Embedded Engineer | Automotive Embedded Systems`.

**Header:** name, headline, then `Ballari, Karnataka | +91 79755 12403 | <email, clickable> | [icon] LinkedIn | [icon] GitHub`. LinkedIn/GitHub are clickable labels (icon + word), not raw URLs; email is shown and clickable. No portfolio URL (not deployed).

---

```
MOHAMMED SHABAZ S
Embedded Engineer | Automotive Embedded Systems
Ballari, Karnataka | +91 79755 12403 | md.shabaz.2005@gmail.com | LinkedIn | GitHub

SUMMARY
Final-year Electronics & Communication Engineering student (CGPA 8.38) focused on embedded
and automotive firmware — ARM Cortex-M microcontroller systems, finite-state machines and
non-blocking real-time design in Embedded C/C++ on ESP32 and STM32 — with a working software
and computer-vision foundation in Python. Internship experience at Nokia and iHelp Robotics.

TECHNICAL SKILLS
Languages: C, C++, Embedded C, Python, SQL
Embedded & Firmware: Microcontrollers, ARM Cortex-M4, finite-state machines, non-blocking
  real-time design, GPIO, I2C, ADC, timers, sensor interfacing, debugging
Platforms & Tools: ESP32, STM32 (Nucleo-L476RG), STM32CubeIDE, Arduino, Android Studio, Git & GitHub
Libraries & Foundations: OpenCV, TensorFlow Lite · Data Structures & Algorithms, Operating
  Systems, DBMS, Computer Networks

EXPERIENCE
Student Intern                                             16 September 2026 – Present
Nokia Solutions and Networks India                                          Bangalore
- Working as a Student Intern at Nokia.

AI Research Intern – Deep Learning & Model Development   23 March 2026 – 23 August 2026
iHelp Robotics Private Limited · Project: MITRA                                 Remote
- Improved live camera-stream reliability in the MITRA assistive Android app across 2
  video sources (hardware WiFi/RTSP and phone-camera fallback): cut stream search delay,
  persisted the last working transport, and added refresh/stall recovery.
- Engineered a visual-freeze watchdog plus 3 status/guard mechanisms — stream-status and
  cloud-status panels and a WebSocket-gated send guard — and fixed a live-refresh loop
  that recurred after 5 minutes.
- Hardened offline voice commands (offline-preferred recognition with model recovery and
  microphone retry backoff) and verified builds across multiple devices with Gradle
  test/lint/assemble; delivered 6+ app-side improvements while model and backend stayed
  with a separate team.

Student Intern – Skin Disease Classification                        1–30 June 2026
IEEE EMBS Pune Section                                                          Remote
- Trained and evaluated a skin-disease image classifier in a 3-member team during a
  1-month IEEE EMBS internship — model selection, training, evaluation, and Python
  image-processing and testing; delivered a working demo-level workflow.

PROJECTS
Automotive Body Control Module                                                 [GitHub]
ESP32, Arduino/C++, Finite-State Machine, GPIO, I2C OLED
- Programmed an ESP32 body-control module with a 3-state (OFF/ACC/ON) ignition FSM
  driving 6+ vehicle functions: turn indicators, synchronized hazard, brake logic, buzzer
  feedback and an OLED dashboard.
- Architected a non-blocking millis()-based scheduler (zero delay() in the main loop) with
  30 ms brake debouncing, throttled 10 Hz I2C OLED refresh, a clean GPIO abstraction and
  edge-triggered serial logging for deterministic real-time behavior.

Smart Wellness Desk Assistant                                                  [GitHub]
STM32 Nucleo-L476RG (ARM Cortex-M4), STM32 HAL, STM32CubeIDE, Embedded C · College team project
- Interfaced ultrasonic presence and 12-bit ADC temperature sensors, an I2C SSD1306 OLED
  and timer-driven buzzer alerts on an STM32 Nucleo-L476RG (ARM Cortex-M4) using STM32 HAL,
  coordinated by a non-blocking finite-state machine; wired, tested and debugged in
  STM32CubeIDE as part of a college team.

VisionPay — Real-Time Indian Currency Detection                                [GitHub]
Python, OpenCV, TensorFlow Lite, MobileNetV2, Text-to-Speech
- Created an offline, real-time tool that recognizes Indian currency from a live webcam
  and speaks the result aloud for visually impaired users.
- Collected ~400 images per denomination across 6 classes (Rs.10–Rs.500) and trained a
  MobileNetV2 classifier converted to TensorFlow Lite, reporting ~93% validation accuracy.
- Strengthened real-time reliability with 4 mechanisms: confidence/margin gating,
  temporal smoothing, a background class, and an auto-count mode.

EDUCATION
B.E. Electronics & Communication Engineering                             Expected 2027
Ballari Institute of Technology and Management (BITM), Ballari    Final Year · CGPA 8.38
Class 12: 80% · Class 10: 86.88%

LEADERSHIP & ACTIVITIES
- Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM (promoted from Treasurer);
  Treasurer, BITM Robotics Club.
- Google Student Ambassador (2025); Selected Participant, IEEE SPACE 2026 — B.Tech Initiative.
- Embedded AI Systems workshop with STMicroelectronics (DigiToad, 2025); Participant,
  Techzone Nationals 2K25 Hardware Hackathon.

CERTIFICATIONS
Embedded Systems — Internshala Trainings (2025) · Programming in C and C++ with AI · SQL for
Data Analytics with AI · Google Cloud Generative AI — SmartBridge/SmartInternz (2025) ·
Python Programming — EISystems (2024)
```

---

## Notes

- **Positioning pivot:** this master is **embedded/automotive-first** (headline `Embedded Engineer | Automotive Embedded Systems`), software/CV kept as visible secondary evidence. Supersedes the earlier software-first draft.
- **Links (PDF/DOCX):** email, header LinkedIn, header GitHub, and each project "GitHub" are live hyperlinks; header LinkedIn/GitHub are icon+label (no raw URLs). `[GitHub]` marks the right-aligned clickable link per project.
- **Skills = verified, bullet-backed set:** enriched into a JD-mirroring taxonomy where every token is also proven in a bullet — Languages (C, C++, Embedded C, Python, SQL); Embedded & Firmware (Microcontrollers, ARM Cortex-M4, FSM, non-blocking real-time design, GPIO, I2C, ADC, timers, sensor interfacing, debugging); Platforms & Tools (ESP32, STM32 Nucleo-L476RG, STM32CubeIDE, Arduino, Android Studio, Git/GitHub); Libraries & Foundations (OpenCV, TensorFlow Lite; DSA, OS, DBMS, CN). **No** Java/Firebase (removed), **no** ESP8266/Raspberry Pi (not demonstrated), **no** UART/SPI/RTOS/CAN/AUTOSAR/MISRA/ISO 26262/UDS/JTAG/DMA/Linux (learning gaps, never claimed). ARM Cortex-M4 is verified (Smart Wellness = STM32L476RG Cortex-M4).
- **Projects shown (embedded-first):** Automotive BCM, Smart Wellness Desk Assistant (team), VisionPay. **AEGIS is omitted** — it is `PLANNED` (not built) and off-domain for an embedded/automotive resume; MITRA sits under the iHelp experience; Skin Disease Classification under the IEEE EMBS experience.
- **Languages section dropped** and Nokia kept to one confidential/high-level line to preserve one-page density and signal-per-line.
- **AEGIS** must never appear as completed. Nokia dates are always `16 September 2026 – Present`.
- Regenerate after edits: `python3 scripts/build_resume.py` then `python3 scripts/validate_resume.py`.
