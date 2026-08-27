# Resume ATS Analysis & Readiness Methodology

How the master resume is evaluated, and how it maps to each target role. This is analysis, not a claim of any commercial ATS score. There is no universal ATS score; different platforms (Workday, Greenhouse, Lever, iCIMS, Taleo) score differently.

## Readiness methodology (defensible, reproducible)

The automated check ([`../scripts/ats_check.py`](../scripts/ats_check.py)) extracts the **actual text** from the generated PDF (via PyMuPDF) and scores six weighted, testable dimensions. It measures parseability and relevance — not a guarantee of any vendor's score.

| Dimension | Weight | What it tests |
|---|---|---|
| Parseability | 25 | Text is selectable/extractable; one page; no image-only content; no multi-column hazards |
| Contact & links | 10 | Name, email, phone, LinkedIn, GitHub present and hyperlinks live |
| Standard sections | 15 | Summary, Education, Skills, Experience, Projects, Leadership, Certifications detected by heading |
| Keyword coverage | 30 | Share of the target-role keyword set present (averaged across the three role sets) |
| Evidence & specificity | 10 | Presence of concrete technical terms and verified quantifiers (e.g. ~93%, 15-stage) |
| Hygiene | 10 | Consistent dates, no parsing traps, links resolve, no fabricated-metric patterns |

**Score = weighted sum, 0–100.** It is an internal *readiness* indicator with a shown breakdown, not "your Workday score." The script prints the per-dimension numbers so the total is auditable.

## Role keyword sets (used for coverage)

Only keywords Shabaz can support with real experience are counted as "covered." Missing-but-learnable keywords are listed as gaps, never added as fake skills.

### A. Software Developer / Software Engineer
- **Core (supported):** C, C++, Python, Java, SQL, Git, GitHub, Android, Android Studio, REST, OpenCV, Firebase, Data Structures, Algorithms, DBMS, Operating Systems, Computer Networks, testing, debugging.
- **Supported via projects/experience:** MobileNetV2, TensorFlow Lite, RTSP, WebSocket, computer vision, mobile app.
- **Gaps (roadmap, not on resume as skills):** OOP depth, system design, concurrency, Linux, CI/CD.

### B. Embedded / Embedded Software Engineer
- **Core (supported):** Embedded C, microcontrollers, ESP32, STM32, firmware, state machine, GPIO, I2C, OLED, ADC, timers, sensors, debugging, testing.
- **Gaps (roadmap):** RTOS/FreeRTOS, UART/SPI/CAN as claimed skills, JTAG/SWD, DMA, bootloaders, embedded Linux, device drivers.

### C. Automotive Embedded / Automotive Software
- **Core (supported):** Automotive (Body Control Module), ESP32, Embedded C, state machine, real-time event loop, firmware.
- **Gaps (roadmap):** CAN, LIN, UDS, AUTOSAR, MISRA, ISO 26262, ASPICE — awareness-only; kept off the resume until learned.

## Per-role mapping (honest fit)

| Role | Keyword match | Skills match | Project relevance | Experience relevance | Education | Top weakness |
|---|---|---|---|---|---|---|
| Software Developer | High | Good (foundational) | High (VisionPay, MITRA) | High (Nokia, iHelp) | Relevant (ECE) | DSA depth; no system design |
| Embedded Engineer | Medium–High | Good | High (Automotive BCM, Smart Wellness) | Medium (embedded via projects) | Strong (ECE) | No RTOS; protocols limited to I2C |
| Automotive Embedded | Medium | Basic-fit | Medium–High (Automotive BCM) | Low direct | Strong (ECE) | No CAN/AUTOSAR/ISO 26262 |

## Tailoring the one master into role versions

Change emphasis only — never facts (see [`resume-strategy.md`](resume-strategy.md)).

- **Software/Android:** promote MITRA and VisionPay to the top of Projects/Experience emphasis; move software skills first; keep AEGIS as an in-progress platform.
- **Embedded:** lead Projects with Automotive BCM, then Smart Wellness Desk Assistant (team project); move Embedded C + Microcontrollers to the front of Skills.
- **Automotive embedded:** lead with Automotive BCM; state CAN/LIN/AUTOSAR/ISO 26262 only in a cover letter as *learning targets*, never as resume skills.

## Honest limitations

- Metrics are limited because most of Shabaz's work is not yet independently benchmarked; the resume uses technical specificity instead of invented numbers.
- Embedded/automotive protocol and RTOS keywords are deliberately absent from Skills because they are not yet held. This lowers raw keyword coverage for those roles but keeps the resume truthful — the correct trade-off.
