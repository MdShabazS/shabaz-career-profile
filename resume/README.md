# Resume

- [master-resume.md](master-resume.md) — the **single master resume source of truth** (content).
- [resume-strategy.md](resume-strategy.md) — rules, ATS approach, and how role versions are derived.
- [ats-analysis.md](ats-analysis.md) — role-specific keyword coverage and the readiness-scoring methodology.
- **Mohammed_Shabaz_S_Master_Resume.pdf** / **.docx** — generated, ATS-friendly, one page, selectable text, clickable links.

## Regenerate

```
python3 scripts/build_resume.py   # writes the PDF and DOCX from master-resume.md content
python3 scripts/ats_check.py      # extracts PDF text and prints the readiness breakdown
```

Facts here must always match the canonical files under `../profile`, `../experience`, `../projects`, `../skills`, `../certifications`, and `../PROFILE.md`. Edit content in `build_resume.py` + `master-resume.md` together, then rebuild.
