# Resume ATS Analysis & Readiness Methodology

How the master resume is evaluated and how it maps to each target role. This is analysis, **not** a claim of any commercial ATS score — there is no universal ATS score; platforms (Workday, Greenhouse, Lever, iCIMS, Taleo) score differently. A content coach such as Resume Worded weights writing quality (impact/verbs) far more than parseability, so scores differ by design.

## Readiness methodology (defensible, reproducible)

[`../scripts/validate_resume.py`](../scripts/validate_resume.py) extracts the **actual text** from the generated PDF (PyMuPDF), writes a `.txt`, and scores seven weighted dimensions that sum to 100.

| Dimension | Weight | What it tests |
|---|---|---|
| Parseability | 20 | 1 page; selectable/extractable text; ≥3 live links |
| Contact & links | 10 | name, email, phone, LinkedIn + GitHub hyperlinks |
| Standard sections | 15 | Summary, Skills, Experience, Projects, Education, Leadership, Certifications detected |
| Keyword coverage | 25 | share of supported role keywords present (avg of 3 roles) |
| Evidence & specificity | 10 | concrete tech terms + verified quantifiers present |
| Quantified impact | 10 | fraction of bullets containing a number |
| Hygiene / writing | 10 | no fabricated precise %, no verb over-use, valid links |

**Score = weighted sum (0–100)**, printed with a per-dimension breakdown so it is auditable. Current: **~96/100**, with Quantified impact intentionally partial (~64% of bullets carry a number — Nokia has no metric by design).

## Representative-JD keyword analysis

Keywords drawn from current 2026 Tier-1 job descriptions. "Present?" = appears in the resume; only keywords Shabaz can genuinely support are counted as covered. Gaps are **learning targets**, never added as fake skills.

### A. Software Engineer
| Keyword | Present? | Where | Strength |
|---|---|---|---|
| C / C++ / Python / Java / SQL | Yes | Skills, bullets | Strong (foundational) |
| Data Structures & Algorithms | Yes | Skills | Basic (learning) |
| Git / GitHub | Yes | Skills, links | Strong |
| Android / Android Studio | Yes | Skills, iHelp/MITRA | Strong |
| OpenCV / computer vision | Yes | Skills, VisionPay | Good |
| TensorFlow Lite / MobileNetV2 | Yes | VisionPay | Good |
| DBMS / OS / Computer Networks | Yes | Skills | Basic |
| testing / debugging | Yes | iHelp, Smart Wellness | Good |
| REST APIs | No | — | **Gap** (not a held skill) |
| OOP / system design / concurrency | No | — | **Gap** (roadmap) |

### B. Embedded Software Engineer
| Keyword | Present? | Where | Strength |
|---|---|---|---|
| Embedded C | Yes | Skills, projects | Good |
| Microcontrollers / ESP32 / STM32 | Yes | Skills (MCU), Automotive BCM, Smart Wellness | Good |
| firmware / state machine / FSM | Yes | Automotive BCM | Good |
| GPIO / I2C / OLED / sensors / timers | Yes | Automotive BCM, Smart Wellness | Good |
| real-time / non-blocking scheduler | Yes | Automotive BCM | Good |
| debugging (STM32CubeIDE) | Yes | Smart Wellness | Good |
| UART / SPI / CAN | No | — | **Gap** (only I2C used) |
| RTOS / FreeRTOS | No | — | **Gap** (roadmap) |
| JTAG/SWD / bootloader / DMA | No | — | **Gap** (roadmap) |

### C. Automotive Embedded Engineer
| Keyword | Present? | Where | Strength |
|---|---|---|---|
| Automotive / Body Control Module | Yes | Automotive BCM | Good |
| ESP32 / Embedded C / FSM / ignition | Yes | Automotive BCM | Good |
| real-time firmware / OLED | Yes | Automotive BCM | Good |
| CAN / LIN / UDS | No | — | **Gap** (roadmap) |
| AUTOSAR / MISRA / ISO 26262 / ASPICE | No | — | **Gap** (awareness only) |

## Per-role fit summary

| Role | Keyword match | Skills fit | Project relevance | Experience | Top weakness |
|---|---|---|---|---|---|
| Software Engineer | High | Good (foundational) | High (VisionPay, MITRA) | High (Nokia, iHelp) | DSA depth; no system design |
| Embedded Software Engineer | Med–High | Good | High (Automotive BCM, Smart Wellness) | Medium (via projects) | No RTOS; only I2C among buses |
| Automotive Embedded | Medium | Basic-fit | Med–High (Automotive BCM) | Low direct | No CAN/AUTOSAR/ISO 26262 |

## Tailoring (emphasis only, never facts)

- **Software/Android:** lead Projects with VisionPay; keep MITRA prominent under Experience; move software skills first.
- **Embedded:** lead Projects with Automotive BCM, then Smart Wellness Desk Assistant (team project); Embedded C + Microcontrollers first in Skills.
- **Automotive:** lead with Automotive BCM; mention CAN/AUTOSAR/ISO 26262 only in a cover letter as learning targets, never as resume skills.

## Honest limitations

- Nokia has no metric (one concise line) — this lowers the quantified-impact ratio but is truthful.
- Embedded/automotive protocol and RTOS keywords are deliberately absent from Skills; this caps coverage for those roles but keeps the resume honest — the correct trade-off.
