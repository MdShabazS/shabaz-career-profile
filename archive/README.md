# Archive

The 2026-08-27 rebuild removed material that no longer reflects Shabaz's current direction (Software Developer + Embedded Engineer, Tier-1 focus). Nothing useful was lost: everything below remains recoverable from git history (before the rebuild commit), and any still-useful facts were migrated into the new canonical files.

## Removed and why

- **NexCast Pro** (removed 2026-08-28) — an individual floor-plan projection project (Python, Flask, OpenCV, Tesseract OCR; 1–12 projector-zone layouts; repo `MdShabazS/NexCast_Pro`). Removed from the current profile, projects, resume, portfolio, LinkedIn, and GitHub per the correction pass. Recoverable from git history (project file `projects/nexcast-pro.md` and the earlier profile README).
- **Bharatiya Antariksh Hackathon 2025** (removed 2026-08-28) — an idea-submission / participant entry (19 Sep 2025), never certified in the repo. Removed from current activities and evidence notes. Distinct from IEEE SPACE 2026, which is retained.
- **`experience/pega.md` + Superset Pega drafts** — the Pega National Internship Program is not part of the fixed experience list (Nokia, iHelp Robotics, IEEE EMBS Pune). Removed from the primary profile. If Shabaz still wants it recorded, add it back as a `COMPLETED` training program with its verified 1-month/60-hour details.
- **`healthcare-research/`** — an open-ended "active research initiative" with no defined problem/product. Not part of the current stated direction. The completed, demo-level Skin Disease Classification project is retained in `projects/`.
- **`roadmap/` (Analytics with Annu AI & Data Science)** — a data-science learning path that conflicts with the Software + Embedded Tier-1 direction. Superseded by `skills/tier1-skills-roadmap.md`.
- **`placement/strategy.md`** — BITM-specific placement workflow. Its useful prep content (DSA, SQL, DBMS, OS, CN, Git, project explanation) is covered by the Tier-1 roadmap and resume strategy.
- **`interview-prep/company-specific/`** — a generated, company-specific prep pack referencing Pega and stale skill levels. A derived output, not a source of truth; regenerate from canonical facts when a specific company is targeted.
- **`superset/profile-submission.md` and `superset/README.md`** — a platform-specific submission draft with outdated Intermediate skill levels and Pega. Its verified evidence (certificate issuers, dates, credential IDs, competition/workshop/volunteering details) was migrated into `certifications/`, `professional-activities/`, and `evidence/`.
- **`docs/` (YAML-era governance/schema/status)** — replaced by `governance/` and the new Markdown structure.
- **`scripts/validate_repo.rb`** — validated the old YAML schema and encoded now-outdated invariants (e.g. MITRA "Navigation module", Intermediate skills). Retired with the YAML format. A Markdown-oriented validator can be added later if desired.

## Retained as evidence

Certificate and proof PDFs moved from `superset/certificates/` to [`../evidence/`](../evidence/).
