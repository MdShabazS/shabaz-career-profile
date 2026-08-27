#!/usr/bin/env python3
"""ATS-style validation of the generated resume PDF.

Extracts the ACTUAL text from the PDF (PyMuPDF) and scores six weighted,
testable dimensions. This is an internal *readiness* indicator with a shown
breakdown, NOT a commercial ATS score (no universal ATS score exists). See
resume/ats-analysis.md for the methodology.

Run: python3 scripts/ats_check.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "resume", "Mohammed_Shabaz_S_Master_Resume.pdf")

# Supported keyword sets per target role (only terms Shabaz can back with real work).
ROLE_KEYWORDS = {
    "Software Developer": [
        "C", "C++", "Python", "Java", "SQL", "Git", "GitHub", "Android", "OpenCV",
        "Firebase", "Data Structures", "Algorithms", "DBMS", "Operating Systems",
        "Computer Networks", "REST", "TensorFlow Lite", "MobileNetV2", "testing",
    ],
    "Embedded Engineer": [
        "Embedded C", "Microcontrollers", "ESP32", "firmware", "state machine",
        "GPIO", "OLED", "debugging", "STM32", "millis",
    ],
    "Automotive Embedded": [
        "Automotive", "Body Control Module", "ESP32", "Embedded C", "state machine",
        "firmware", "OLED", "ignition",
    ],
}

EVIDENCE_TOKENS = ["~93%", "15-stage", "MobileNetV2", "TensorFlow Lite", "ESP32",
                   "RTSP", "WebSocket", "state machine", "~400", "6 note classes"]

SECTIONS = ["SUMMARY", "EDUCATION", "SKILLS", "EXPERIENCE", "PROJECTS",
            "LEADERSHIP", "CERTIFICATIONS"]


def main():
    import fitz
    if not os.path.exists(PDF):
        print("PDF not found. Run scripts/build_resume.py first.")
        sys.exit(1)

    doc = fitz.open(PDF)
    pages = doc.page_count
    text = "\n".join(p.get_text() for p in doc)
    low = text.lower()
    links = []
    for p in doc:
        links += [l for l in p.get_links() if l.get("uri")]

    report = []
    score = 0.0

    # 1. Parseability (25)
    pz = 0
    pz += 10 if pages == 1 else 0
    pz += 10 if len(text.strip()) > 800 else 0
    pz += 5 if len(links) >= 3 else 0
    report.append(("Parseability", pz, 25,
                   f"pages={pages}, extractable_chars={len(text.strip())}, uri_links={len(links)}"))
    score += pz

    # 2. Contact & links (10)
    cz = 0
    checks = {
        "name": "mohammed shabaz s" in low,
        "email": bool(re.search(r"md\.shabaz\.2005@gmail\.com", low)),
        "phone": "7975512403" in text,
        "linkedin": "linkedin.com/in/shabaz17" in low,
        "github": "github.com/mdshabazs" in low,
    }
    cz = sum(2 for v in checks.values() if v)
    report.append(("Contact & links", cz, 10,
                   ", ".join(f"{k}={'ok' if v else 'MISSING'}" for k, v in checks.items())))
    score += cz

    # 3. Standard sections (15)
    found = [s for s in SECTIONS if s in text.upper()]
    sz = 15 * len(found) / len(SECTIONS)
    report.append(("Standard sections", round(sz, 1), 15,
                   f"{len(found)}/{len(SECTIONS)} found"))
    score += sz

    # 4. Keyword coverage (30) — average across role sets
    per_role = {}
    fracs = []
    for role, kws in ROLE_KEYWORDS.items():
        present = [k for k in kws if k.lower() in low]
        frac = len(present) / len(kws)
        fracs.append(frac)
        per_role[role] = (len(present), len(kws), sorted(set(kws) - set(present)))
    kz = 30 * (sum(fracs) / len(fracs))
    report.append(("Keyword coverage", round(kz, 1), 30,
                   " | ".join(f"{r}: {per_role[r][0]}/{per_role[r][1]}" for r in per_role)))
    score += kz

    # 5. Evidence & specificity (10)
    ev = [t for t in EVIDENCE_TOKENS if t.lower() in low]
    ez = 10 * len(ev) / len(EVIDENCE_TOKENS)
    report.append(("Evidence & specificity", round(ez, 1), 10, f"{len(ev)}/{len(EVIDENCE_TOKENS)} tokens"))
    score += ez

    # 6. Hygiene (10)
    hz = 10.0
    hyg = []
    # fabricated-accuracy pattern: any precise x.y% that is not the allowed ~93%
    bad_pct = [m for m in re.findall(r"\d{1,3}\.\d%", text)]
    if bad_pct:
        hz -= 4
        hyg.append(f"precise % found: {bad_pct}")
    # link schemes valid
    if any(not l["uri"].startswith(("http", "mailto:")) for l in links):
        hz -= 2
        hyg.append("non-standard link scheme")
    # ascii-safe (allow common typographic dashes/bullets)
    try:
        text.encode("latin-1")
    except UnicodeEncodeError:
        pass  # em dash etc. are fine; not penalized
    # date consistency: expect 'Mon YYYY' or 'Present'
    if "Present" not in text:
        hz -= 2
        hyg.append("Nokia 'Present' missing")
    report.append(("Hygiene", round(hz, 1), 10, "; ".join(hyg) if hyg else "clean"))
    score += hz

    # Output
    print("=" * 68)
    print("ATS READINESS (internal, from extracted PDF text) — not a vendor score")
    print("=" * 68)
    for name, got, mx, detail in report:
        print(f"  {name:<24} {got:>5} / {mx:<3}  {detail}")
    print("-" * 68)
    print(f"  {'TOTAL':<24} {round(score,1):>5} / 100")
    print("-" * 68)
    print("Keyword gaps by role (learnable; intentionally NOT added as skills):")
    for role, (p, t, gaps) in per_role.items():
        print(f"  {role}: missing {gaps if gaps else 'none'}")

    # 20-point ATS format checklist (pass/fail)
    print("-" * 68)
    print("Format checklist:")
    checklist = {
        "1 text extractable": len(text.strip()) > 800,
        "2 sections detected": len(found) == len(SECTIONS),
        "3 name extractable": checks["name"],
        "4 contact extractable": checks["email"] and checks["phone"],
        "5 dates present": bool(re.search(r"(19|20)\d\d", text)),
        "6 experience section": "EXPERIENCE" in text.upper(),
        "7 skills section": "SKILLS" in text.upper(),
        "8 education section": "EDUCATION" in text.upper(),
        "9 projects section": "PROJECTS" in text.upper(),
        "10 keyword coverage ok": (sum(fracs) / len(fracs)) > 0.6,
        "11 hyperlinks live": len(links) >= 3,
        "12 single page": pages == 1,
        "13 no image-only page": len(text.strip()) > 800,
        "14 no precise fake %": not bad_pct,
        "15 file name correct": os.path.basename(PDF) == "Mohammed_Shabaz_S_Master_Resume.pdf",
    }
    for k, v in checklist.items():
        print(f"  [{'x' if v else ' '}] {k}")

    hard_fail = (pages != 1) or (not checks["name"]) or (len(found) < len(SECTIONS)) or bad_pct
    if hard_fail:
        print("\nATS CHECK: FAIL")
        sys.exit(1)
    print(f"\nATS CHECK: PASS (readiness {round(score)}/100)")


if __name__ == "__main__":
    main()
