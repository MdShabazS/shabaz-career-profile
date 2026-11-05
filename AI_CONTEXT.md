# AI Context

First file any AI system (Claude, ChatGPT, Codex) should read. This repository is Mohammed Shabaz S's private career source of truth. Use it to generate resumes, portfolio copy, LinkedIn/GitHub text, interview prep, and gap analysis — not as a creative biography.

## Non-negotiable rules

- Never invent facts. Missing info is `Not yet known` or `TO_VERIFY`.
- Never convert `PLANNED`/`UPCOMING` → completed, `LEARNING`/`BASIC` → advanced, internship → employment, team → individual, or reported/estimated metric → verified.
- Never expose confidential Nokia or MITRA information ([`governance/CONFIDENTIALITY.md`](governance/CONFIDENTIALITY.md)).
- Never invent certificate issuers, dates, awards, metrics, technologies, titles, responsibilities, team sizes, or model architectures.
- Keep external research ([`research/`](research/)) separate from Shabaz's facts. Market requirements never become his credentials.
- Spell the name exactly: **Mohammed Shabaz S**.

## Canonical ownership (one fact, one file)

- Identity / positioning / contact / education / languages / interests → [`profile/`](profile/)
- Experience → [`experience/`](experience/) (order: Nokia, iHelp Robotics, IEEE EMBS Pune)
- Projects → [`projects/`](projects/) (5 current projects: AEGIS, MITRA, VisionPay, Automotive BCM, Smart Wellness Desk Assistant; exclusions in [`projects/EXCLUDED.md`](projects/EXCLUDED.md))
- Current skills → [`skills/current-skills.md`](skills/current-skills.md); LTE/5G study completed during Nokia internship → [`skills/mobile-networks.md`](skills/mobile-networks.md); future/target skills → [`skills/tier1-skills-roadmap.md`](skills/tier1-skills-roadmap.md)
- Certifications → [`certifications/certifications.md`](certifications/certifications.md)
- Leadership / memberships → [`leadership/`](leadership/)
- Activities → [`professional-activities/`](professional-activities/)
- Resume rules + master → [`resume/`](resume/)
- Evidence PDFs → [`evidence/`](evidence/)

When files overlap, prefer the canonical owner and flag any contradiction instead of inventing a merge.

## Key boundaries (memorize)

- **Nokia:** current Student Intern (16 Sep 2026 – Present), Bangalore. The assigned project/domain remains `Not yet known` / confidential. User confirms LTE/5G study as part of the internship; keep any description to those high-level training topics and do not expose internal material. Never a fixed end date; never describe the internship as completed.
- **iHelp / MITRA:** completed internship (23 Mar – 23 Aug 2026), official title "AI Research Intern – Deep Learning & Model Development", project MITRA. App-side software/Android contribution only; backend/model belonged to another team. Present primarily as Software/Android, not AI/ML. MITRA is the project name and is shown under the iHelp experience, not as a standalone personal project.
- **IEEE EMBS:** retain the one-month remote internship record (1–30 June 2026) and certificate evidence. The associated project has been removed from current project/profile outputs.
- **AEGIS:** individual project; design/planning complete, coding not started, no target date, hardware not finalized. The emergency-response concept is accurate. AI recommends; a human dispatcher reviews, decides, and dispatches.
- **VisionPay:** individual; ~93% accuracy is reported, not verified; training code AI-assisted.
- **Automotive BCM:** completed individual ESP32 project using Arduino/C++; includes OFF/ACC/ON FSM, indicators/synchronized hazards, brake logic, buzzer/OLED, non-blocking `millis()` loop, 30 ms brake debounce, 10 Hz OLED refresh, and zero `delay()` calls in the main loop.
- **Smart Wellness Desk Assistant:** completed college team project on STM32 Nucleo-L476RG with STM32 HAL/STM32CubeIDE; team size not specified. Shabaz handled sensor interfacing, wiring, testing, and debugging.
- **Skills:** C/C++/Python/SQL Intermediate; Java currently learning/not yet proficient; DSA/DBMS/OS/CN Basic. Embedded C and Microcontrollers Intermediate. Git/GitHub are current. Android Studio belongs only under MITRA; OpenCV only under VisionPay. LTE/5G study was completed during the Nokia internship; it is not a credential. Do not list boards individually as current skills.
- **Excluded / removed:** NIDAR and an undocumented hackathon project stay out of the primary profile. NexCast Pro and Pega are removed from the current profile (historical note in `archive/`).

## Output discipline

Resumes/portfolio/LinkedIn are outputs generated from canonical facts. Do not edit a canonical fact to fit an output. Follow [`resume/resume-strategy.md`](resume/resume-strategy.md) and [`portfolio/portfolio-requirements.md`](portfolio/portfolio-requirements.md). Record meaningful changes in [`governance/CHANGELOG.md`](governance/CHANGELOG.md).
