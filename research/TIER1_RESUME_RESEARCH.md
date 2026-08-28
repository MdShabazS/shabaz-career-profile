# Tier-1 Resume Research (2026) — Embedded / Automotive Primary

Research behind the master resume. Primary target: **Embedded Engineer | Automotive Embedded Systems**. Secondary target: **Software Engineering**. Format for each finding: **SOURCE → FINDING → WHY IT MATTERS → HOW IT AFFECTS THIS RESUME.** Three label types are kept strictly separate:

- `USER FACT` — a verified fact about Mohammed Shabaz S (from this repo / user confirmation). Never invented.
- `RESEARCH` — an external market/ATS finding. Never becomes a fact about Shabaz.
- `RECOMMENDATION` — a resume decision derived from combining the two.

Role-requirement research lives in [`TIER1_ROLE_RESEARCH.md`](TIER1_ROLE_RESEARCH.md); this file is resume-construction-specific. Accessed **2026-08-28**. Coach/aggregator sites are directional; the strongest signals are cross-confirmed across several independent sources and against real job descriptions.

---

## 0. Positioning pivot (this build)

- `USER FACT` (2026-08-28): The primary target is **Embedded Engineer / Automotive Embedded Systems**; software engineering is the secondary target. Headline is **"Embedded Engineer | Automotive Embedded Systems."** This overrides the earlier software-first positioning in the repo's older resume drafts.
- `RECOMMENDATION`: Lead the Summary and the Technical-Skills block with embedded/automotive terms; order Projects embedded-first (Automotive BCM → Smart Wellness → VisionPay); keep the software/CV work as visible secondary evidence, not the spine.

## 1. Old-resume analysis (the ~83 template)

The prior PDF Shabaz attached is used **only** as a design/layout reference. Its *facts* were stale (Pega present, iHelp shown as "Present", Nokia missing, and ESP32/STM32/REST/Java listed as standalone skills).

**What it did well (keep):**
- Centered header: bold all-caps name + a single one-line positioning subtitle.
- Section headers in small navy caps with a full-width horizontal rule — very fast to scan.
- Right-aligned dates and locations per entry — a clean two-column *feel* while the underlying text stays single-column and linearly parseable.
- Quantified, specific bullets ("2 video sources", "6+ functions", "~93%", "3-state", "15-stage").
- Project entries with a repo link and an italic tech-stack line.
- Dense but readable; fit exactly one page.

**What must NOT be copied:**
- Any stale fact: Pega, NexCast, "iHelp – Present", missing Nokia.
- Skills line listing `ESP32, STM32 (Nucleo-L476RG), STM32CubeIDE, STM32 HAL, Arduino IDE, I2C, timers` as **skills** — these are `USER FACT` platforms he used, but per the locked skills policy they belong in **project bullets**, not the Skills section.
- `Java` and `Firebase, REST APIs` as headline skills — dropped from the current locked skill set (2026-08-28 user list).
- The multi-line SUMMARY that leaned software-first.

## 2. Length, layout, file format

- **SOURCE:** BeamJobs & Enhancv embedded-SWE guides 2026; Jobscan ATS-format 2026; Merit America 2026 resume tips.
  - `RESEARCH`: One page for a candidate with internships; reverse-chronological; **single column**; standard fonts; **no tables/graphics/skill-bars/columns** that break parsing. ATS read content linearly (left→right, top→bottom); columns and text boxes are the most common parse-breakers.
  - **WHY IT MATTERS:** A two-column layout can scramble the reading order so a parser interleaves a skills column into experience bullets, destroying keyword→context mapping.
  - `RECOMMENDATION`: One page, single visual column. Right-aligned dates are implemented as a flex row (title left / date right) that still extracts as one line — never a page-level multi-column grid. Ship a **text-based PDF** (selectable text, live links) plus a **DOCX**.

- **SOURCE:** HiroCV / Resumemate PDF-vs-DOCX 2026.
  - `RESEARCH`: Modern ATS (Workday, Greenhouse, Lever, iCIMS, Taleo) parse both; a text PDF is safe for direct upload; DOCX is the conservative default and is what staffing agencies request.
  - `RECOMMENDATION`: Ship both. The validator extracts the PDF text to a `.txt` to prove it is real text, not an image.

## 3. Section order & the Summary question

- **SOURCE:** BeamJobs / Enhancv new-grad & embedded guides 2026; SWEResume new-grad guide.
  - `RESEARCH`: For students/new grads, **Projects** is a first-class section and the Skills block is parsed early. A short, *specific* summary helps keyword placement; generic "passionate engineer" objectives hurt.
  - `RECOMMENDATION`: Order = **Summary → Technical Skills → Experience → Projects → Education → Leadership & Activities → Certifications.**
    - Experience stays above Projects because Nokia and iHelp are real, named-brand industry internships — the highest-credibility anchor a recruiter scans for first.
    - The Summary and Skills are written embedded/automotive-first so the embedded signal is already dense in the top third, before the reader reaches the (embedded-heavy) Projects block.
    - Education sits after Projects: for a final-year student a strong CGPA (8.38) is an asset, but on an embedded resume the firmware projects out-signal the degree line, so they come first.

- **SOURCE:** Enhancv embedded 2026 (skills-grouping pattern).
  - `RESEARCH`: Strong embedded resumes group skills into categories that mirror JD structure — Languages, MCU/MPU, Protocols, RTOS/OS, Tools & IDEs, Standards & Compliance.
  - **WHY IT MATTERS:** Category headers that match JD phrasing raise exact-keyword hit-rate.
  - `RECOMMENDATION`: Adopt the *grouping idea* but only populate categories Shabaz genuinely holds — Languages; Embedded; Tools & Platforms; CS Fundamentals. **Protocols/RTOS/Standards are intentionally NOT category headers** because their contents are learning gaps; inventing an empty-looking "Protocols: I2C" line to chase the pattern would be dishonest keyword-stuffing. I2C/GPIO/ADC/FSM appear where they were actually used — in project bullets.

## 4. Bullets — quantification & verb variety (the 52 → 82 lesson)

- **SOURCE:** Resume Worded score methodology 2026 (impact/quantification, weak & repeated verbs, passive voice, buzzwords); WahResume quantified-achievements 2026; the prior 52-scoring AI draft's failure mode.
  - `RESEARCH`: Content scorers weight **quantified impact** heavily and penalize **repeated/weak action verbs** and passive voice. Testing shows the single biggest score lever is **adding exact-phrase required skills from the JD** — larger than any formatting fix (>10× the smallest lever).
  - **WHY IT MATTERS:** The 52 draft over-used "Built/Added" and quantified <45% of bullets. Verb variety + honest numbers are the two biggest *honestly-fixable* levers.
  - `RECOMMENDATION`:
    - Every bullet opens with a **distinct** verb (Programmed, Architected, Interfaced, Engineered, Hardened, Trained, Collected, Improved, Leading, Working). No verb repeats.
    - Surface only **real** repo numbers: 3-state FSM, 6+ functions, non-blocking `millis()` scheduler, 2 sensor types, I2C OLED, ~400 images/denomination, 6 classes, 4 reliability mechanisms, ~93% reported, 2 video sources, 5-minute loop fix, 6+ app-side improvements, 3-member team, 15-stage. **No fabricated metrics.** Nokia carries no number by design (confidential, high-level) — one concise line.
    - Bullet shape target: **Action + technical implementation + engineering context + result/evidence.**

## 5. Keywords vs. honesty (the core constraint)

- **SOURCE:** japply ATS-keywords for Embedded SWE 2026; Enhancv/ResumeGeni embedded ATS 2026; real automotive JDs — Ford (AUTOSAR BSW), Qorvo (Sr. Automotive Embedded), Mobileye (AUTOSAR); Qualcomm/NVIDIA new-grad embedded postings.
  - `RESEARCH`: Embedded/automotive postings search exact terms: **C, C++, Embedded C, RTOS/FreeRTOS, firmware, device drivers, BSP, HAL, microcontroller, ARM Cortex-M, UART, SPI, I2C, CAN, LIN, GPIO, ADC, PWM, interrupts, debugging (JTAG/SWD, Trace32), Git.** Automotive adds **AUTOSAR, MISRA C, ISO 26262 / functional safety / ASIL, ASPICE, Vector CANoe/CANalyzer, diagnostics/UDS.**
  - **WHY IT MATTERS:** Missing the exact token can drop the resume below an ATS keyword threshold — but fabricating held skills fails the first technical screen and is disqualifying at Tier-1.
  - `RECOMMENDATION` (the honesty firewall):
    - **Honestly present (in Skills and/or bullets):** C, C++, Embedded C, Python, SQL, microcontrollers, firmware, finite-state machine, GPIO, I2C, ADC, timers, real-time/non-blocking design, debugging, Git/GitHub, OpenCV, TensorFlow Lite, MobileNetV2, Android.
    - **Honestly present in bullets only (real platforms used, not Skills-section claims):** ESP32, STM32 Nucleo-L476RG, STM32CubeIDE/HAL, OLED, ultrasonic + ADC temperature sensing, RTSP.
    - **NEVER add (learning gaps, logged in [`../skills/tier1-skills-roadmap.md`](../skills/tier1-skills-roadmap.md)):** RTOS/FreeRTOS, UART/SPI as claimed competencies, CAN/LIN, AUTOSAR, MISRA, ISO 26262, ASPICE, UDS, JTAG/SWD, DMA, bootloaders, embedded Linux, device drivers/BSP. These belong in a cover letter as *targets*, never on the resume as skills.
    - **Component inventory** (ESP32/MCP2515/TJA1050/NRF24L01/etc.) proves *intent to build*, not experience — excluded until a verified project exists.

## 6. Header / contact / links

- **SOURCE:** Jobscan ATS-format 2026; user instruction (2026-08-28).
  - `RESEARCH`: ATS needs a literal email and working profile links; long raw URLs clutter a header and waste line width.
  - `RECOMMENDATION`: Header shows a clickable **LinkedIn** and **GitHub** *label* (small mono-tone icon + the word), and a clickable email; the underlying `https://…` and `mailto:` targets stay machine-readable in the PDF/DOCX. No portfolio URL (not deployed — do not invent one). Phone shown as plain text (some ATS mis-parse tel: links).

## 7. Project selection & ordering (embedded-first)

- `USER FACT`: Six projects exist; AEGIS is `PLANNED` (design stage, not built); Automotive BCM, Smart Wellness (college team), VisionPay, Skin Disease Classification (team, demo-level) are `COMPLETED`; MITRA sits under the iHelp experience.
  - `RESEARCH`: Automotive/embedded recruiters weight *relevant, completed, firmware* projects highest; a planned or off-domain project is weak top-of-resume signal.
  - `RECOMMENDATION` — ranked by embedded/automotive hiring signal:
    1. **Automotive Body Control Module (ESP32)** — the single most on-target artifact: automotive domain + FSM + non-blocking real-time firmware. **Lead project.**
    2. **Smart Wellness Desk Assistant (STM32 Nucleo-L476RG)** — second embedded proof: peripheral interfacing (ultrasonic, ADC, I2C OLED, timers) + STM32CubeIDE debugging. Labeled a **college team project**.
    3. **VisionPay** — secondary-target (software/CV) proof with the resume's one real metric (~93% reported); shows Python/TensorFlow Lite/OpenCV breadth.
    - **AEGIS: omit from the embedded master.** It is planned (not completed) and its domain is AI emergency-response, not embedded/automotive — low embedded signal for a one-page embedded resume. Its leadership value is already captured by the Leadership section and the iHelp/BITM roles. (Include only on a software/systems-leaning version if space allows, always labeled in-progress.)
    - Skin Disease Classification stays under the IEEE EMBS experience line, not as a standalone project.

## 8. Sections to compress or cut (one-page economics)

- `RESEARCH`: On a one-page Tier-1 technical resume, spoken-language lists and long certification lists are low signal-per-line.
  - `RECOMMENDATION`:
    - **Spoken Languages:** cut the standalone section (proficiencies are `TO_VERIFY`; lowest signal-per-line). Reclaim the space for embedded evidence.
    - **Certifications:** keep, but compressed to **one wrapped line**; lead with **Embedded Systems (Internshala, 2025)** because it is on-target, then the rest for keyword breadth.
    - **Leadership & Activities:** compress to **two lines** (three roles on one; IEEE SPACE 2026 + Google Student Ambassador on the next).
    - **Nokia:** keep to **one line** (confidential/high-level) — do not pad.

## 9. ATS "score" honesty

- **SOURCE:** Resume Optimizer Pro "what is a good ATS score" 2026; Jobscan; Resume Worded.
  - `RESEARCH`: There is **no** universal ATS score — Workday/Greenhouse/Lever/iCIMS/Taleo score differently, and content coaches (Resume Worded/Jobscan) weight writing quality far more than raw parseability.
  - `RECOMMENDATION`: Never print a fabricated commercial score. Publish an **internal, auditable "ATS-Style Readiness Score"** ([`../resume/ats-analysis.md`](../resume/ats-analysis.md)) with explicit weighted dimensions computed by [`../scripts/validate_resume.py`](../scripts/validate_resume.py), and separately estimate likely Resume Worded/Jobscan behaviour without claiming a guaranteed number.

---

### Sources (accessed 2026-08-28)
- [Enhancv — Embedded Software Engineer resume 2026](https://enhancv.com/resume-examples/embedded-software-engineer/)
- [BeamJobs — Embedded Software Engineer resume 2026](https://www.beamjobs.com/resumes/embedded-software-engineer-resume-examples)
- [Resume Worded — Embedded System Engineer resume example](https://resumeworded.com/embedded-system-engineer-resume-example)
- [Resume Worded — Embedded SWE skills & keywords](https://resumeworded.com/skills-and-keywords/embedded-software-engineer-skills)
- [japply — Embedded Software Engineer ATS keywords 2026](https://japply.io/ats-keywords/embedded-software-engineer)
- [ResumeGeni — Embedded Systems Engineer ATS resume guide](https://resumegeni.com/blog/embedded-systems-engineer-resume-guide)
- [Ford — Embedded Software Engineer (AUTOSAR BSW) JD](https://www.careers.ford.com/en/job/dearborn/embedded-software-engineer-autosar-bsw/48560/95089590720)
- [Qorvo — Sr. Automotive Embedded Software Engineer JD](https://careers.qorvo.com/job/Sr_-Automotive-Embedded-Software-Engineer-FL/1209474100/)
- [Mobileye — AUTOSAR Embedded Software Engineer JD (Built In)](https://builtin.com/job/autosar-embedded-software-engineer-m-w-d/10499277)
- [Qualcomm — Embedded Systems Software Engineer JD (Dice)](https://www.dice.com/job-detail/451e4e83-808f-44f4-bb58-0481f8cf969e)
- [Teal — Automotive Embedded Engineer resume example](https://www.tealhq.com/resume-example/automotive-embedded-engineer)
- [Jobscan — ATS-friendly resume format/templates 2026](https://www.jobscan.co/blog/20-ats-friendly-resume-templates/)
- [HiroCV — resume file format PDF vs DOCX 2026](https://hirocv.com/blog/resume-file-format-pdf-vs-docx)
- [Resumemate — PDF vs DOCX 2026](https://www.resumemate.io/blog/pdf-vs-docx-for-resumes-in-2025-what-recruiters-ats-really-prefer/)
- [Resume Optimizer Pro — what is a good ATS score (2026)](https://resumeoptimizerpro.com/blog/what-is-a-good-ats-resume-score)
- [WahResume — quantified achievements, action verbs & metrics 2026](https://www.wahresume.com/blog/master-quantified-achievements-action-verbs-metrics-2026)
- [Merit America — resume tips 2026 + ATS checklist](https://meritamerica.org/blog/resume-tips-2026-free-templates-ats-checklist/)
