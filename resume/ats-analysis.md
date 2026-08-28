# Resume ATS Analysis & Readiness Methodology

How the master resume is evaluated and how it maps to each target role. This is analysis, **not** a claim of any commercial ATS score — there is no universal ATS score; platforms (Workday, Greenhouse, Lever, iCIMS, Taleo) score differently, and a content coach such as Resume Worded weights writing quality (impact/verbs) far more than parseability, so scores differ by design. Primary target: **Embedded Engineer / Automotive Embedded Systems**; secondary: **Software Engineering**.

## ATS-Style Readiness Score (internal, defensible, reproducible)

[`../scripts/validate_resume.py`](../scripts/validate_resume.py) extracts the **actual text** from the generated PDF (PyMuPDF), writes a `.txt`, and scores seven weighted dimensions that sum to 100. It is printed with a per-dimension breakdown so it is auditable — it is **not** a Resume Worded / Jobscan number.

| Dimension | Weight | What it tests |
|---|---|---|
| Parseability | 20 | 1 page; selectable/extractable text; ≥3 live links |
| Contact & links | 10 | name, email, phone, LinkedIn + GitHub hyperlinks |
| Standard sections | 15 | Summary, Skills, Experience, Projects, Education, Leadership, Certifications detected |
| Keyword coverage | 25 | share of *supportable* role keywords present (avg of 5 target roles) |
| Evidence & specificity | 10 | concrete tech terms + verified quantifiers present |
| Quantified impact | 10 | fraction of bullets containing a number |
| Hygiene / writing | 10 | no fabricated precise %, no verb over-use, valid links |

**Current result: ~97/100** (Quantified impact ~71% of bullets; Nokia is one confidential line with no metric by design).

### External-style JD alignment (the honest ~85 answer)
The internal readiness score above only counts *supportable* keywords, so it runs high (~97). External tools (Jobscan/Resume Worded targeted match) score a resume against a **whole JD, including terms the candidate lacks** — which is why the real external number was ~85, not 96. `validate_resume.py` now also prints an **external-style JD alignment** using representative full 2026 Tier-1 keyword sets (gaps included):

| Target role | Alignment | Main missing (genuine gaps) |
|---|---|---|
| Embedded Engineer | **~79%** | UART, SPI, RTOS, interrupts |
| Embedded Software Engineer | **~74%** | RTOS, UART, SPI, device drivers, Linux |
| Automotive Embedded Engineer | **~68%** | CAN, AUTOSAR, MISRA, ISO 26262, UDS, diagnostics |
| Automotive Software Engineer | **~65%** | CAN, AUTOSAR, MISRA, ISO 26262, ASPICE, Vector CANoe |
| Software Engineer (secondary) | **~85%+** | REST APIs, OOP, system design |

This optimization pass raised embedded/firmware alignment (added the verified **ARM Cortex-M4**, **STM32CubeIDE**, **Arduino**, **GPIO/I2C/ADC/timers/sensor interfacing** as JD-mirroring skills, all also proven in bullets) — the biggest honest lever from ~85. The automotive ceiling (~65–68%) is real: it is gated by CAN/AUTOSAR/MISRA/ISO 26262, which cannot be added without a verified project. Closing them (e.g. the planned MCP2515/TJA1050 CAN build) is the only honest way past it.

### Skills-section design note (why it is fuller, not stuffed)
Research finding (Jobscan 2026 playbook): flat lists of **>20** skills raise rejection; keywords score best when they appear in **both** a categorized skills block **and** the bullets. So the enriched Skills section is a focused, JD-mirroring taxonomy (Languages / Embedded & Firmware / Platforms & Tools / Libraries & Foundations) where **every token is also evidenced in a project or experience bullet** — richer match without a keyword dump.

### What the keyword dimension does and does NOT count
The 25-point keyword dimension scores only terms Shabaz can **genuinely support**. Advanced specialization terms he does not hold (RTOS/FreeRTOS, UART/SPI as claimed skills, CAN/LIN, AUTOSAR, MISRA, ISO 26262, ASPICE, UDS, JTAG/SWD, DMA, bootloaders, device drivers) are tracked as **learning gaps** and are **never** added to the resume or counted as coverage. This keeps the score honest: it measures how well the *true* profile is surfaced, not how many buzzwords were stuffed.

### Likely behaviour on Resume Worded / Jobscan-style tools
- **Format/parse checks:** should score very high — single column, standard headings, selectable text, clean links, one page (the levers those tools reward most).
- **Content score (Resume Worded):** strong on verb variety (every bullet a distinct verb) and evidence; capped only by the honest ~64% quantified ratio and the deliberately foundational skill levels. Realistic band: **high (≈ mid-80s to low-90s)**, not a guaranteed number.
- **Jobscan match rate:** depends entirely on the pasted JD. Against a foundational embedded JD (C/Embedded C, microcontrollers, firmware, FSM, GPIO, I2C, debugging, Git) match is high; against an AUTOSAR/CAN/ISO 26262 automotive JD it will be **moderate**, because those are real gaps — the correct, honest outcome.

## Representative-JD keyword matrix (2026 Tier-1)

"Present?" = appears in the resume; "Strength" reflects real depth. Gaps are **learning targets**, never added as fake skills. Sources in [`../research/TIER1_RESUME_RESEARCH.md`](../research/TIER1_RESUME_RESEARCH.md).

### A. Embedded Software / Systems Engineer
| Keyword | Present? | Evidence | Strength | Gap / learning target |
|---|---|---|---|---|
| Embedded C | Yes | Skills, both embedded projects | Good | — |
| Microcontrollers / ESP32 / STM32 | Yes | Skills (MCU), Automotive BCM, Smart Wellness | Good | — |
| firmware / finite-state machine / FSM | Yes | Automotive BCM | Good | — |
| GPIO / I2C / ADC / OLED / timers / sensors | Yes | Automotive BCM, Smart Wellness | Good | — |
| real-time / non-blocking scheduler | Yes | Automotive BCM | Good | — |
| debugging (STM32CubeIDE) | Yes | Smart Wellness | Good | — |
| C / C++ / Git | Yes | Skills, bullets | Good | — |
| UART / SPI | No | only I2C used | — | **Gap** (P0 roadmap) |
| RTOS / FreeRTOS | No | — | — | **Gap** (P1 roadmap) |
| JTAG/SWD / DMA / bootloader / device drivers / BSP | No | — | — | **Gap** (P1–P2 roadmap) |

### B. Automotive Embedded / Software Engineer
| Keyword | Present? | Evidence | Strength | Gap / learning target |
|---|---|---|---|---|
| Automotive / Body Control Module | Yes | Automotive BCM | Good | — |
| ESP32 / Embedded C / ignition FSM | Yes | Automotive BCM | Good | — |
| real-time firmware / OLED / GPIO | Yes | Automotive BCM | Good | — |
| testing / debugging | Yes | iHelp, Smart Wellness | Good | — |
| CAN / LIN / FlexRay | No | — | — | **Gap** (automotive P2) |
| AUTOSAR (BSW/RTE) | No | — | — | **Gap** (P3 awareness) |
| MISRA C | No | — | — | **Gap** (P2 awareness) |
| ISO 26262 / functional safety / ASIL | No | — | — | **Gap** (P3 awareness) |
| ASPICE / UDS / Vector CANoe | No | — | — | **Gap** (P3 awareness) |

### C. Software Engineer (secondary target)
| Keyword | Present? | Evidence | Strength | Gap / learning target |
|---|---|---|---|---|
| C / C++ / Python / SQL / Git | Yes | Skills, bullets | Good | — |
| Android / Android Studio | Yes | iHelp/MITRA | Strong | — |
| OpenCV / computer vision | Yes | VisionPay | Good | — |
| TensorFlow Lite / MobileNetV2 | Yes | VisionPay | Good | — |
| DSA / DBMS / OS / Computer Networks | Yes | Skills | Basic | depth (P0–P1 roadmap) |
| testing / debugging | Yes | iHelp, projects | Good | — |
| REST APIs / OOP / system design | No | — | — | **Gap** (roadmap) |

## Per-role fit summary

| Role | Keyword match | Skills fit | Project relevance | Experience | Top weakness |
|---|---|---|---|---|---|
| Embedded Software Engineer | Med–High | Good | High (Automotive BCM, Smart Wellness) | Medium (via projects) | No RTOS; only I2C among buses |
| Embedded Systems Engineer | Med–High | Good | High | Medium | No UART/SPI/RTOS depth |
| Automotive Embedded Engineer | Medium | Basic-fit | Med–High (Automotive BCM) | Low direct | No CAN/AUTOSAR/ISO 26262 |
| Automotive Software Engineer | Medium | Good (C/Embedded C) | Med–High | Low direct | No AUTOSAR/MISRA toolchain |
| Software Engineer (secondary) | High | Good (foundational) | High (VisionPay, MITRA) | High (Nokia, iHelp) | DSA depth; no system design |

## Tailoring (emphasis only, never facts)

- **Embedded / Automotive (primary):** lead Projects with Automotive BCM → Smart Wellness; Embedded + Microcontrollers first in Skills; mention CAN/AUTOSAR/ISO 26262 only in a cover letter as learning targets, never as resume skills.
- **Software / Android (secondary):** promote VisionPay and the iHelp/MITRA Android work; move Languages/Tools ahead of Embedded in Skills; keep the same facts.

## Honest limitations

- Nokia carries no metric (one confidential line) — lowers the quantified-impact ratio but is truthful.
- Automotive protocol/AUTOSAR/functional-safety keywords are deliberately absent — this caps automotive keyword coverage but keeps the resume honest and interview-safe. That is the correct trade-off for a Tier-1 target.
