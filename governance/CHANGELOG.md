# Changelog

## 2026-08-28 — Final correction pass

Applied the latest user-confirmed corrections and prepared channel-ready content.

- **Education:** added Final Year; CGPA 8.38 is now stated as current and verified (removed "may change / TO_VERIFY" language).
- **Nokia:** changed to **16 September 2026 – Present** (current), removed the fixed end date and "upcoming" framing.
- **iHelp Robotics:** clarified MITRA as the project name (not the designation); MITRA presented under the iHelp experience.
- **Projects:** now exactly 6, ordered AEGIS, MITRA, VisionPay, Automotive BCM, Smart Wellness Desk Assistant, Skin Disease Classification. **Removed NexCast Pro** from the current profile. AEGIS marked Planned/In Progress (intended flagship once completed).
- **Current skills:** locked to the finalized list; embedded shown as "Embedded C, Microcontrollers" (no individual boards); confirmed all levels Basic.
- **Leadership:** reordered to IEEE CAS Vice-Chair, BITM Robotics Club Treasurer, Google Student Ambassador.
- **IEEE SPACE 2026:** removed the report-submission claim.
- **Certifications:** list limited to the 5 confirmed; removed the planned-certifications list; certs 1–2 issuer/date marked "not yet provided" (cert itself confirmed).
- **Removed** Bharatiya Antariksh Hackathon from current activities/evidence (historical note in `../archive/README.md`).
- **Added:** master `PROFILE.md`, LinkedIn-ready content (`linkedin/`), GitHub profile README draft (`github/`), and an automated validator (`scripts/validate.py`). Updated resume, portfolio requirements, README, AI_CONTEXT, and source index.
- Commit: `fix: finalize current career profile and professional positioning`.

## 2026-08-27 — Rebuild as single source of truth

Full audit and restructure. See [`../AUDIT_REPORT.md`](../AUDIT_REPORT.md) for the complete list.

Highlights:

- Restructured from mixed YAML/Markdown into one clean Markdown source of truth with a two-axis status system (fact confidence + lifecycle).
- **Experience:** replaced the Pega program with the Nokia internship as a top experience; fixed order Nokia → iHelp Robotics → IEEE EMBS Pune. Added Nokia (Student Intern, 16 Sep 2026 – 14 Aug 2027, upcoming) and updated iHelp Robotics with its official designation, dates (23 Mar – 23 Aug 2026, completed), and the detailed confirmed app-side work.
- **Skills:** corrected programming levels to Basic (C, C++, Python, Java, SQL) — previously Intermediate; kept DSA/DBMS/OS/CN Basic. Added the Tier-1 skills roadmap (future skills, kept separate from current).
- **Leadership:** reduced to three positions; removed AEGIS Team Lead from Leadership (AEGIS remains a project).
- **Profile:** set location to Ballari (not Bangalore); added contact details; replaced interests with Embedded Systems, Automotive, AI/ML, Technology Events & Conferences.
- **Certifications:** moved "SQL for Data Analytics with AI" and "Programming in C and C++ with AI" to completed (evidence `TO_VERIFY`); migrated issuer/date/credential details for the three evidenced certificates.
- **Professional activities:** added IEEE SPACE 2026 (Selected Participant), plus competitions/workshops/volunteering with evidence.
- **Added:** research/, portfolio requirements, resume strategy + rebuilt master resume, governance/.
- **Retired:** healthcare-research initiative, the Analytics-with-Annu data-science roadmap, BITM placement strategy, the generated company-specific interview-prep, and the old Superset submission draft (stale skill levels/Pega). Recoverable via git history; see [`../archive/README.md`](../archive/README.md).
- Moved certificate PDFs from `superset/certificates/` to `evidence/`.
