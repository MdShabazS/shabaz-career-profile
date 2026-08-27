# Tier-1 Resume Research (2026)

Research behind the master resume. Format: **source → finding → why it matters → how it affects this resume.** `USER FACT` / `RESEARCH` / `RECOMMENDATION` are kept separate. Research never becomes a fact about Shabaz. Role-requirement research lives in [`TIER1_ROLE_RESEARCH.md`](TIER1_ROLE_RESEARCH.md); this file is resume-specific.

Accessed 2026-08-28. Aggregator/coach sites are treated as directional; the strongest signals are cross-confirmed across several.

---

## 0. Old-resume analysis (the ~83 template)

The prior resume (attached by Shabaz) is used **only** as a design/layout reference; its facts were outdated (Pega present, iHelp "Present", Nokia missing, ESP32/STM32/REST listed as skills).

**What it did well (kept):**
- Centered navy header; name in bold caps; a one-line positioning subtitle.
- Section headers in small navy caps with a full-width rule — fast to scan.
- Right-aligned dates and locations per entry — clean two-column *feel* while staying single-column text.
- Quantified, specific bullets (e.g. "2 video sources", "6+ app-side capabilities", "~93%", "3-state / 6+ functions", "15-stage").
- Project entries with a repo link and an italic tech-stack line.
- Dense but readable; fit one page.

**What it needed fixing (done):**
- `USER FACT`: current facts — Nokia (Sep 2026–Present), iHelp completed with full title, MITRA as the project, Pega/NexCast removed, 5 certifications, locked skills (Microcontrollers, all Basic, no REST/boards/RTOS).
- Skills section trimmed to the locked list; specific platforms (ESP32/STM32/I2C/TensorFlow Lite) moved into project bullets only.
- `RECOMMENDATION`: keep the layout, replace the facts, and header LinkedIn/GitHub become clickable **labels with icons** (not raw URLs).

## 1. Length, layout, format

- **Source:** BeamJobs / Enhancv new-grad & embedded resume guides 2026; Jobscan ATS format 2026.
  - **Finding (RESEARCH):** One page for a candidate with internships; reverse-chronological; single column; standard fonts; **no tables/graphics/columns** that break parsing; single-column layouts parse far more reliably.
  - **How it affects this resume (RECOMMENDATION):** One page, single column. Right-aligned dates use a borderless two-cell row (text still extracts linearly), not a page-level multi-column layout. Output as selectable-text PDF + DOCX.

- **Source:** HiroCV / Resumemate PDF-vs-DOCX 2026.
  - **Finding (RESEARCH):** Modern ATS (Workday, Greenhouse, Lever, iCIMS, Taleo) read both; a **text-based PDF** is safe for direct submission, **DOCX** is the conservative default and is requested by staffing agencies.
  - **RECOMMENDATION:** Ship both; verify the PDF text is extractable (validator writes a `.txt`).

## 2. Section order and summary

- **Source:** SWEResume / BeamJobs / Enhancv new-grad guides 2026.
  - **Finding (RESEARCH):** Projects are a top section for new grads; the Skills section is parsed early; a short, specific summary aids keyword placement (generic "passionate" objectives hurt).
  - **RECOMMENDATION:** Order = Summary → Technical Skills → Experience → Projects → Education → Leadership & Activities → Certifications → Languages (matches the proven template). Summary is 3 lines, specific, no buzzwords.

## 3. Bullets — quantification and verb variety (the 52→ lesson)

- **Source:** Resume Worded score report on the prior generated resume; Enhancv/BeamJobs embedded 2026.
  - **Finding (RESEARCH):** Content scorers weight **quantified impact** heavily and penalize **repeated action verbs** (the earlier draft over-used "Built"/"Added" and had only ~40% quantified bullets, scoring 52). They also expect exact-term keywords (name MCUs/protocols in bullets).
  - **Why:** These are the two biggest, honestly-fixable levers on writing-quality scorers.
  - **How it affects this resume (RECOMMENDATION):**
    - Every bullet starts with a distinct verb (Improved, Engineered, Hardened, Trained, Developed, Collected, Programmed, Architected, Interfaced, Leading, Working).
    - Surface only **real** numbers already in the repo: 2 video sources, 3 status/guard mechanisms, 5-minute loop fix, 6+ app-side improvements, ~400 images, 6 classes, 4 reliability mechanisms, ~93%, 3-state / 6+ functions, 2 sensor types, 3-member team, 15-stage. Quantified-bullet ratio raised to ~64%.
    - **No fabricated metrics.** Nokia has no number (kept to one concise line). Where no metric exists, use technical specificity.

## 4. Keywords vs honesty

- **Source:** Enhancv embedded 2026; ResumeGeni embedded ATS 2026.
  - **Finding (RESEARCH):** Postings search for exact MCU families (STM32/ESP32) and protocols (SPI/I2C/UART/CAN).
  - **RECOMMENDATION:** `USER FACT` — the Skills section stays on the locked list (Microcontrollers; no unheld protocols/RTOS). Exact platforms Shabaz *did* use (ESP32, STM32, I2C, OLED, TensorFlow Lite, MobileNetV2) appear in **project/experience bullets**, giving ATS the exact terms honestly. Unheld terms (RTOS, CAN/LIN, AUTOSAR, MISRA, ISO 26262) are logged as learning gaps, never added.

## 5. Header / contact

- **Source:** Jobscan ATS format 2026; user instruction (2026-08-28).
  - **Finding (RESEARCH):** ATS needs a literal email and working profile links; long raw URLs clutter the header.
  - **How it affects this resume (RECOMMENDATION):** Header shows clickable **LinkedIn** and **GitHub** labels (with small icons) instead of raw URLs; email is shown and clickable; hyperlink targets remain machine-readable. No portfolio URL is invented.

*Sources:* [BeamJobs new-grad SWE 2026](https://www.beamjobs.com/resumes/software-engineer-new-grad-resume-examples); [Enhancv new-grad SWE 2026](https://enhancv.com/resume-examples/software-engineer-new-grad/); [Enhancv embedded SWE 2026](https://enhancv.com/resume-examples/embedded-software-engineer/); [BeamJobs embedded SWE 2026](https://www.beamjobs.com/resumes/embedded-software-engineer-resume-examples); [SWEResume new-grad guide](https://www.sweresume.app/articles/new-grad-resume-guide/); [HiroCV file format 2026](https://hirocv.com/blog/resume-file-format-pdf-vs-docx); [Resumemate PDF vs DOCX 2026](https://www.resumemate.io/blog/pdf-vs-docx-for-resumes-in-2025-what-recruiters-ats-really-prefer/); [Jobscan ATS format 2026](https://www.jobscan.co/blog/20-ats-friendly-resume-templates/).
