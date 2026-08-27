# Tier-1 Role Research (2026)

**External research only.** This file records what the market expects. It never establishes a fact about Shabaz. Requirements here feed the gap analysis in [`../skills/tier1-skills-roadmap.md`](../skills/tier1-skills-roadmap.md); Shabaz's actual skills are in [`../skills/current-skills.md`](../skills/current-skills.md).

Accessed: 2026-08-27. Sources are listed per section; treat aggregator/blog sources as directional and official career pages as primary.

---

## Role A — Tier-1 Software Developer (new-grad / early-career)

**Recurring requirements**

- **DSA is the primary filter.** At major Tier-1 companies, coding rounds (typically ≥2) test data structures and algorithms at LeetCode medium–hard difficulty; online assessments are timed. System-design exposure for new grads is minimal but a differentiator.
- **Fundamentals:** solid grasp of one language (Java/Python/C++), OOP, DBMS/SQL, operating systems, computer networks, testing, and version control (Git).
- **SDLC participation:** design, implementation, testing, deployment, and support are listed responsibilities.
- **Skills section on the resume is parsed first** on major ATS (Greenhouse, Workday) — use full tool names.
- **Soft skills:** communication, willingness to learn, teamwork, time management.

**Relevance to Shabaz:** matches the Software Developer track. He has Basic C/C++/Python/Java/SQL and Basic DSA/DBMS/OS/CN, plus Git and project experience (NexCast Pro APIs, MITRA app work).

**Resulting skill gap:** raise DSA from Basic to interview-ready; pick and deepen one language; turn Basic DBMS/OS/CN into working interview knowledge; add OOP; strengthen testing and Linux. (P0/P1 in the roadmap.)

*Sources:* [Indeed — 2026 new grad SWE jobs](https://www.indeed.com/q-2026-new-grad-software-engineer-jobs.html); [ZipRecruiter — key skills for new-grad SWE](https://www.ziprecruiter.com/e/What-are-the-key-skills-and-qualifications-needed-to-thrive-in-the-Full-Time-New-Grad-Software-Engineer-position-and-why-are-they-important); [Interview Kickstart — FAANG DSA questions 2026](https://interviewkickstart.com/blogs/interview-questions/faang-dsa-interview-questions); [TechScreen — new-grad SWE interview guide 2026](https://techscreen.app/articles/new-grad-software-engineer-interview-guide-2026).

---

## Role B — Tier-1 Embedded Engineer (entry-level)

**Recurring requirements**

- **Strong C is the #1 hiring filter.** C/C++ fluency, pointers, and memory are non-negotiable.
- **MCU + ARM Cortex-M** architecture knowledge; comfort with a real toolchain.
- **Peripherals & protocols:** GPIO, ADC, timers/counters, interrupts, PWM, plus **UART, SPI, I2C** (and CAN for automotive/industrial).
- **RTOS** (FreeRTOS, ThreadX, Zephyr) — mandatory in automotive, robotics, and industrial roles.
- **Low-level debugging** with JTAG/SWD; bootloaders and firmware architecture; power optimization.
- **Embedded Linux / device drivers** for Linux-class devices (role-dependent).
- **Verification** (unit, integration, HIL) is the most effort-intensive part of safety-critical work.

**Relevance to Shabaz:** matches the Embedded Engineer track and the Embedded/Automotive interests. He has hands-on ESP32/STM32/Arduino exposure (Automotive BCM, Smart Wellness Desk Assistant) with incidental I2C/ADC/timers usage.

**Resulting skill gap:** deepen C; move peripheral exposure to confident interrupt-driven UART/SPI/I2C work; add RTOS/FreeRTOS; adopt hardware debugging (JTAG/SWD); learn bootloaders/DMA. (P0/P1 in the roadmap.)

*Sources:* [Interview Kickstart — 9 embedded SWE skills 2026](https://interviewkickstart.com/skills/embedded-software-engineer); [Jobicy — embedded systems developer career 2026](https://jobicy.com/careers/embedded-systems-developer); [Cranes Varsity — essential embedded skills 2026](https://cranesvarsity.com/essential-technical-skills-for-embedded-systems-engineers-in-2026/).

---

## Role B (specialization) — Automotive embedded

**Recurring requirements**

- **Safety & process standards:** ISO 26262 (functional safety, ASIL levels) for safety, and ASPICE for process quality — usually applied together.
- **Coding standards:** MISRA C (and AUTOSAR C++14 / CERT in OEM-custom standards).
- **AUTOSAR** architecture awareness; **CAN/LIN** networking; diagnostics.
- **Verification-heavy:** unit testing, static analysis, HIL, MC/DC coverage, traceability.

**Relevance to Shabaz:** Automotive is a stated interest and Automotive BCM is a portfolio project. For entry level, awareness of these frameworks is a differentiator, not a gate.

**Resulting skill gap:** awareness-level understanding of CAN/LIN, MISRA C, and ISO 26262/ASPICE vocabulary — deepen only when targeting automotive roles. (P2/P3 in the roadmap.)

*Sources:* [AUTOSAR.io — ISO 26262 guide](https://autosar.io/en/insights/iso26262-guide); [Parasoft — ISO 26262 software compliance](https://www.parasoft.com/learning-center/iso-26262/what-is/); [QA Systems — ISO 26262 testing best practices](https://www.qa-systems.com/blog/iso-26262-testing-best-practices/).

---

## Engineering portfolio expectations (2026)

**Recurring guidance**

- Project-first, one-page feel; top 3 projects with role and stack visible without scrolling.
- Every project needs a working GitHub repo or live demo — a dead link reads as abandoned work.
- Outcomes beat verbs ("cut p95 latency from 800ms to 120ms" > "worked on performance").
- Recruiters scan for 5–10 seconds; the site's own performance and mobile experience are themselves signals (a 3-second load is an anti-signal).

**Relevance / recommendation:** the portfolio requirements ([`../portfolio/portfolio-requirements.md`](../portfolio/portfolio-requirements.md)) already target fast, responsive, project-first design. Use real repos/media only; where a metric is only reported (e.g. VisionPay ~93%), present it as reported, not verified.

*Sources:* [Zencoder — SWE portfolio 2026](https://zencoder.ai/blog/how-to-create-software-engineer-portfolio); [Hakia — developer portfolio guide 2026](https://hakia.com/skills/building-portfolio/); [SitesPlaced — best SWE portfolios 2026](https://sitesplaced.com/blog/best-portfolio-website-for-software-engineers).

---

## Resume / ATS expectations (2026)

**Recurring guidance**

- 1–2 pages; single-column; **no tables, columns, graphics, logos, charts, or photos** (parsers drop them).
- Standard fonts; consistent job-title formatting; write full terms with acronyms ("Computer Networks (CN)").
- The **Skills section is parsed first** on Greenhouse/Workday — list full tool names.
- Keyword location matters: summary and the first bullet under each role are weighted higher.
- Evidence (tools, scale, outcomes) beats keyword stuffing.

**Relevance / recommendation:** reflected in [`../resume/resume-strategy.md`](../resume/resume-strategy.md) — one page, one column, no decorative elements, keyword-aligned to the target JD, using only verified facts.

*Sources:* [Jobscan — ATS-friendly resume format 2026](https://www.jobscan.co/blog/20-ats-friendly-resume-templates/); [Resume Optimizer Pro — ATS best practices 2026](https://resumeoptimizerpro.com/blog/ats-friendly-resume-tips); [Resume Vera — SWE resume guide 2026](https://resumevera.com/blogs/software-engineer-resume-guide-2026).
