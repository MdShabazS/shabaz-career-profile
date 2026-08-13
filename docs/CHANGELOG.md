# Changelog

## 2026-08-13

- Added `superset/` for non-sensitive Superset placement profile submission records.
- Stored the professional Superset summary and upload checklist while excluding sensitive personal fields.
- Added curated Superset certificate proofs and an index for certifications, internships, workshops, competitions, awards, and volunteering.
- Updated Superset profile drafts to reflect final submission decisions, including no public MITRA/AEGIS links and excluding NexCast Pro from Superset projects.
- Added `resume/MASTER_RESUME.md` as the ATS-oriented reusable resume base for future company-specific tailoring.
- Revised the master resume wording with stronger action verbs and verified quantified details for ATS scoring.
- Reduced repeated resume verbs and added additional verified quantified details for the ATS V3 resume.
- Added recruiter contact details and clickable public profile/project links to the master resume.

## 2026-08-09

- Established the repository as an AI-optimized career knowledge base.
- Added explicit fact status governance.
- Added structured profile, skills, project facts, healthcare research, and validation files.
- Preserved AEGIS architecture baseline and human-dispatcher responsibility boundary.
- Preserved MITRA backend/model ownership boundary.
- Marked NIDAR and undocumented hackathon project as excluded.

## V1.0 Refinement

- Standardized project status modeling with separate `fact_status`, `evidence_status`, and `lifecycle_status` fields.
- Added evidence tracking without inventing supporting artifacts.
- Added `docs/SOURCE_INDEX.md` as the central source/evidence map.
- Corrected healthcare research state to `ACTIVE_RESEARCH_INITIATIVE`.
- Corrected language modeling so language existence is verified while proficiency remains `TO_VERIFY`.
- Preserved AEGIS canonical architecture formatting with `→` arrows.
- Explicitly represented NexCast Pro web UI.
- Established the canonical rule that project `facts.yaml` files are structured source-of-truth records.
