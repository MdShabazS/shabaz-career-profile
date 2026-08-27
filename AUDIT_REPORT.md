# Audit Report — 2026-08-27 Rebuild

> **Superseded in part by the 2026-08-28 correction pass.** This report documents the original rebuild. For the current state and the corrections applied afterward (Nokia = Present, CGPA 8.38 finalized, Final Year, projects reduced to 6, NexCast Pro / Bharatiya Antariksh removed, skills finalized, leadership reordered, master `PROFILE.md` + LinkedIn/GitHub content + validator added), see [`governance/CHANGELOG.md`](governance/CHANGELOG.md) and [`PROFILE.md`](PROFILE.md).

Full audit and rebuild of the career profile repository into a single source of truth. This documents what changed and what remains open.

## 1. Files created

- `README.md` (rewritten), `AI_CONTEXT.md` (rewritten)
- `profile/`: identity.md, professional-positioning.md, contact.md, education.md, languages.md, interests.md
- `experience/`: README.md, nokia.md, ihelp-robotics.md (rewritten), ieee-embs-pune.md
- `projects/`: README.md, aegis.md, mitra.md, skin-disease-classification.md, nexcast-pro.md, visionpay.md, automotive-bcm.md, smart-wellness-desk-assistant.md, EXCLUDED.md (rewritten)
- `skills/`: current-skills.md, tier1-skills-roadmap.md
- `certifications/certifications.md`
- `leadership/`: leadership.md, memberships.md
- `professional-activities/`: README.md, ieee-space-2026.md, competitions-and-workshops.md
- `resume/`: README.md, resume-strategy.md, master-resume.md
- `portfolio/`: README.md, portfolio-requirements.md
- `research/TIER1_ROLE_RESEARCH.md`
- `governance/`: STATUS_SYSTEM.md, DATA_POLICY.md, CONFIDENTIALITY.md, UPDATE_RULES.md, SOURCE_INDEX.md, CHANGELOG.md
- `evidence/INDEX.md` (rewritten), `archive/README.md`, `AUDIT_REPORT.md`

## 2. Files updated

- Certificate/proof PDFs relocated (git-tracked renames) from `superset/certificates/` → `evidence/`.
- README, AI_CONTEXT, experience/ihelp-robotics.md, projects/EXCLUDED.md, evidence/INDEX.md rewritten to current truth.

## 3. Files deleted (content migrated first; recoverable via git history)

- `profile/*.yaml`, `skills/*.yaml`, `skills/proficiency.md`
- `experience/experience-index.yaml`, `experience/ieee-embs.md`, `experience/pega.md`
- `projects/<Project>/README.md` + `facts.yaml` (all 7), `projects/project-priority.yaml`
- `certifications/completed.yaml`, `certifications/planned.yaml`
- `achievements/`, `leadership/positions.yaml`, `memberships/memberships.yaml`
- `resume/MASTER_RESUME.md`, `resume/instructions.md`
- `docs/` (6 files), `healthcare-research/` (2), `placement/strategy.md`, `interview-prep/` (2), `scripts/validate_repo.rb`, `roadmap/` (16)
- `superset/profile-submission.md`, `superset/README.md`

## 4. Information migrated

- Certificate issuers/dates/credential IDs and competition/workshop/volunteering details from the old Superset submission → `certifications/`, `professional-activities/`, `evidence/INDEX.md`.
- Project facts (stack, features, boundaries) from `facts.yaml` files → per-project Markdown.
- AEGIS locked architecture and responsibility model → `projects/aegis.md`.
- MITRA/iHelp boundaries and the new detailed confirmed work → `experience/ihelp-robotics.md`, `projects/mitra.md`.

## 5. Contradictions resolved

| Was | Now | Basis |
|---|---|---|
| Programming C/C++/Python Intermediate | Basic (all of C/C++/Python/Java/SQL) | Latest user-confirmed brief |
| Pega listed as current experience | Removed from primary; Nokia added | Fixed experience list |
| iHelp "Mar 2026 – Present" | Completed 23 Mar – 23 Aug 2026 | Confirmed dates + today's date |
| MITRA work incl. navigation/OCR/wake-word | Replaced with the detailed confirmed app-side list | Latest explicit user list supersedes |
| Leadership includes AEGIS Team Lead | Leadership = 3 roles; AEGIS is a project | Brief Part 9 |
| Location "Bellary" / Bangalore usage | Ballari as profile location; Bangalore only for work locations | Brief Part 3 |
| Interests: Gaming, Travelling | Embedded Systems, Automotive, AI/ML, Tech Events | Brief Part 13 |
| SQL / C&C++ certs "planned" | Completed (evidence `TO_VERIFY`) | Brief Part 11 |
| NexCast Pro "internship project" | Individual project (internship context `TO_VERIFY`) | Brief Part 6 |

## 6. Remaining `TO_VERIFY`

- Certifications 1–2 (SQL for Data Analytics with AI; Programming in C and C++ with AI): issuer, exact title, date; no certificate attached.
- Nokia project domain/team (confidential; not yet known).
- IEEE SPACE 2026 certificate.
- Skin Disease Classification exact model.

## 7. Confidentiality checks

- Nokia kept high-level; no domain, code, tooling, customer, or implementation detail. Domain left `Not yet known`.
- MITRA described only via Shabaz's high-level app-side contributions; backend/model attributed to another team; no proprietary internals; no public repo link.
- No offer letters, IDs, phone-in-plaintext-public, passwords, or tokens committed. Phone marked non-public for web outputs.
- Secret scan: no keys/tokens present (checked before commit).

## 8. Current skills (verified)

C, C++, Python, Java, SQL — Basic. DSA, DBMS, OS, CN — Basic. Hands-on: ESP32, STM32, Arduino, Raspberry Pi, Embedded C, Android Studio, OpenCV, Firebase, Git/GitHub. Project-demonstrated tools listed as exposure only.

## 9. Future skills (targets, not claims)

Captured in `skills/tier1-skills-roadmap.md` with P0–P3 ranking: DSA depth, OOP, working DBMS/OS/CN, testing, APIs, Linux, system design (software); strong C, Cortex-M, UART/SPI/I2C, interrupts/timers/ADC/PWM, RTOS/FreeRTOS, JTAG/SWD, DMA, bootloaders, embedded Linux (embedded); CAN/LIN, MISRA, ISO 26262/ASPICE/AUTOSAR awareness (automotive).

## 10. Experience timeline

- iHelp Robotics — 23 Mar – 23 Aug 2026 (~5 months) — `COMPLETED`.
- IEEE EMBS Pune — 1–30 June 2026 (1 month) — `COMPLETED`.
- Nokia — 16 Sep 2026 – Present — `CURRENT` (updated in the 2026-08-28 pass; originally recorded as upcoming with an end date).
- Internship/industry experience only. No full-time employment claimed.

## 11. Project status verification

AEGIS `PLANNED` (design stage) · MITRA `COMPLETED` (internship) · Skin Disease Classification `COMPLETED` (demo-level team) · NexCast Pro `COMPLETED` (individual) · VisionPay `COMPLETED` (individual; ~93% reported) · Automotive BCM `COMPLETED` (individual) · Smart Wellness Desk Assistant `COMPLETED` (team). NIDAR + undocumented hackathon `EXCLUDED`.

## 12. Portfolio readiness

Requirements captured in `portfolio/portfolio-requirements.md` (content, design, accessibility, performance, SEO, contact, writing style). Site not built (per scope). Pending real media: MITRA screenshots, IEEE SPACE 2026 photographs, other project media.

## 13. Resume readiness

Master resume source of truth rebuilt (`resume/master-resume.md`) with strategy and ATS rules. Accurate to current facts. No PDF built (per scope). Default top-3 AEGIS/Automotive BCM/MITRA, with substitution rule when AEGIS must not appear as completed.

## 14. Tier-1 skill gaps

See item 9 and `research/TIER1_ROLE_RESEARCH.md`. Biggest levers: strong C/C++ or Java + DSA + Git (shared P0 base); software fundamentals depth; embedded peripheral/RTOS/debugging depth.

## 15. Remaining missing information

- Nokia domain (confidential/unknown).
- Certificate details for items 1–2; several certificates/photographs not yet attached.
- Portfolio media assets.

(Resolved in the 2026-08-28 pass: CGPA 8.38 confirmed current; Final Year set; Nokia = Present; leadership confirmed; NexCast Pro and Bharatiya Antariksh removed.)

## Verification performed before commit

- Internal Markdown links checked (0 broken after this report is added).
- Name spelling verified as "Mohammed Shabaz S" throughout.
- Stale-term scan (Pega, Intermediate, Analytics-with-Annu, Gaming/Travelling, Bangalore-as-location, healthcare) — only intentional historical references remain in `archive/` and `governance/CHANGELOG.md`.
- Planned vs completed, team vs individual, and confidentiality boundaries reviewed per file.
