#!/usr/bin/env python3
"""Validate the generated resume PDF and produce an ATS-readiness assessment.

Extracts the ACTUAL text from the PDF (PyMuPDF), writes a plain-text version,
runs a format/parse checklist, checks facts and leakage, and prints a weighted
readiness score with a full breakdown. This is an internal readiness indicator
with a shown methodology, NOT a commercial ATS score (no universal ATS score
exists). See resume/ats-analysis.md.

Run: python3 scripts/validate_resume.py   (exit 0 = pass, 1 = fail)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "resume", "Mohammed_Shabaz_S_Master_Resume.pdf")
TXT = os.path.join(ROOT, "resume", "Mohammed_Shabaz_S_Master_Resume.txt")

# Keyword lists per target role. Only terms Shabaz can genuinely support are scored here;
# advanced specialization terms (RTOS/CAN/AUTOSAR/MISRA/ISO 26262/...) are tracked as
# learning gaps in ROLE_GAPS below and are deliberately NOT counted as coverage.
ROLE_KEYWORDS = {
    "Embedded Software Engineer": [
        "Embedded C", "Microcontrollers", "ESP32", "STM32", "firmware", "state machine",
        "GPIO", "I2C", "OLED", "ADC", "sensors", "real-time", "debugging", "C", "C++", "Git",
    ],
    "Embedded Systems Engineer": [
        "Embedded C", "Microcontrollers", "ESP32", "STM32", "firmware", "finite-state",
        "GPIO", "I2C", "timers", "sensors", "real-time", "non-blocking", "debugging",
    ],
    "Automotive Embedded Engineer": [
        "Automotive", "Body Control", "ESP32", "Embedded C", "ignition", "FSM",
        "state machine", "real-time", "firmware", "OLED", "GPIO",
    ],
    "Automotive Software Engineer": [
        "Automotive", "Embedded C", "C", "C++", "state machine", "real-time", "firmware",
        "testing", "debugging", "Git",
    ],
    "Software Engineer (secondary)": [
        "C", "C++", "Python", "SQL", "Git", "GitHub", "Android", "OpenCV",
        "Data Structures", "Algorithms", "DBMS", "Operating Systems",
        "Computer Networks", "TensorFlow Lite", "MobileNetV2", "testing", "debugging",
    ],
}

# Advanced terms NOT held — reported as gaps, never scored as coverage, never added as skills.
ROLE_GAPS = {
    "Embedded Software Engineer": ["UART", "SPI", "CAN", "RTOS", "FreeRTOS", "JTAG/SWD", "device drivers"],
    "Embedded Systems Engineer": ["UART", "SPI", "RTOS", "DMA", "bootloader", "JTAG/SWD"],
    "Automotive Embedded Engineer": ["CAN", "LIN", "AUTOSAR", "MISRA", "ISO 26262", "UDS", "ASPICE"],
    "Automotive Software Engineer": ["CAN", "AUTOSAR", "MISRA", "ISO 26262", "Vector CANoe"],
    "Software Engineer (secondary)": ["REST APIs", "OOP", "system design", "concurrency"],
}

EVIDENCE_TOKENS = ["~93%", "MobileNetV2", "TensorFlow Lite", "ESP32", "STM32", "ignition",
                   "3-state", "~400", "6 classes", "2 video sources", "3-member", "I2C", "FSM",
                   "ARM Cortex-M4", "STM32CubeIDE", "12-bit", "30 ms", "10 Hz"]

# External-style JD alignment: representative FULL keyword sets from real 2026 Tier-1 JDs,
# INCLUDING terms Shabaz does not hold. This mimics how Jobscan/Resume Worded match a resume
# against a whole JD, so the % is honest and shows genuine gaps (unlike the internal readiness
# score, which only counts supportable terms). Nothing here is added to the resume.
JD_ALIGNMENT = {
    "Embedded Engineer": [
        "C", "C++", "Embedded C", "microcontroller", "ARM Cortex-M", "firmware", "GPIO",
        "I2C", "ADC", "timers", "state machine", "real-time", "sensors", "debugging", "Git",
        "UART", "SPI", "RTOS", "interrupts",
    ],
    "Embedded Software Engineer": [
        "C", "C++", "Embedded C", "microcontroller", "ARM Cortex-M", "firmware", "RTOS",
        "GPIO", "I2C", "ADC", "debugging", "state machine", "real-time", "Git", "STM32",
        "UART", "SPI", "device drivers", "Linux",
    ],
    "Automotive Embedded Engineer": [
        "Automotive", "Embedded C", "C", "microcontroller", "firmware", "state machine",
        "ESP32", "real-time", "OLED", "GPIO", "debugging", "sensors",
        "CAN", "LIN", "AUTOSAR", "MISRA", "ISO 26262", "UDS", "diagnostics",
    ],
    "Automotive Software Engineer": [
        "Automotive", "C", "C++", "Embedded C", "firmware", "state machine", "real-time",
        "testing", "debugging", "Git", "microcontroller",
        "CAN", "AUTOSAR", "MISRA", "ISO 26262", "ASPICE", "Vector CANoe",
    ],
}

SECTIONS = ["SUMMARY", "TECHNICAL SKILLS", "EXPERIENCE", "PROJECTS", "EDUCATION",
            "LEADERSHIP", "CERTIFICATIONS"]

REMOVED = ["NexCast", "Pega", "Bharatiya"]
FUTURE_AS_SKILL = ["RTOS", "FreeRTOS", "AUTOSAR", "MISRA", "ISO 26262", "ASPICE",
                   "Docker", "CAN", "LIN", "UDS"]


def main():
    import fitz
    if not os.path.exists(PDF):
        print("PDF not found. Run scripts/build_resume.py first.")
        sys.exit(1)

    doc = fitz.open(PDF)
    pages = doc.page_count
    text = "\n".join(p.get_text() for p in doc)
    with open(TXT, "w", encoding="utf-8") as fh:
        fh.write(text)
    low = text.lower()
    flat = re.sub(r"\s+", " ", low)  # whitespace-normalized, like real ATS keyword matching
    upper = text.upper()
    links = [l["uri"] for p in doc for l in p.get_links() if l.get("uri")]

    errors, warns = [], []

    # ---- Contact / identity extraction
    checks = {
        "name": "mohammed shabaz s" in low,
        "email": "md.shabaz.2005@gmail.com" in low,
        "phone": "7975512403" in re.sub(r"[ \-]", "", text),
        "linkedin_link": any("linkedin.com/in/shabaz17" in u for u in links),
        "github_link": any("github.com/mdshabazs" in u.lower() for u in links),
        "email_link": any(u.startswith("mailto:md.shabaz.2005") for u in links),
    }
    for k, v in checks.items():
        if not v:
            errors.append(f"contact/{k} missing")

    # ---- Sections
    found_sections = [s for s in SECTIONS if s in upper]
    for s in SECTIONS:
        if s not in upper:
            errors.append(f"section '{s}' not detected")

    # ---- Education / dates / facts
    fact_checks = {
        "CGPA 8.38": "8.38" in text,
        "Final Year": "Final Year" in text,
        "Expected 2027": "2027" in text,
        "BITM": "Ballari Institute of Technology" in text,
        "Nokia Present": bool(re.search(r"Nokia", text)) and "Present" in text,
        "Nokia exact date": "16 September 2026" in text,
        "iHelp dates": "March 2026" in text and "August 2026" in text,
        "MITRA is project": "Project: MITRA" in text or "MITRA" in text,
    }
    for k, v in fact_checks.items():
        if not v:
            errors.append(f"fact '{k}' missing/incorrect")

    # ---- Nokia confidentiality wording must NOT appear (latest instruction)
    if re.search(r"confidential", low):
        errors.append("confidentiality wording present (should be removed)")

    # ---- Removed projects must not appear
    for term in REMOVED:
        if term.lower() in low:
            errors.append(f"removed item '{term}' present in resume")

    # ---- Future skills must not be in the skills section
    skills_block = ""
    m = re.search(r"TECHNICAL SKILLS(.*?)EXPERIENCE", text, re.S | re.I)
    if m:
        skills_block = m.group(1)
    for term in FUTURE_AS_SKILL:
        if term.lower() in skills_block.lower():
            errors.append(f"future skill '{term}' listed in Skills section")
    # boards should not be bulleted as standalone skills lines
    if re.search(r"(?im)^\s*(ESP32|STM32|Arduino|Raspberry)\s*$", skills_block):
        errors.append("individual board listed as standalone skill")

    # ---- Hyperlinks resolve to expected/valid schemes
    for u in links:
        if not u.startswith(("http://", "https://", "mailto:")):
            errors.append(f"non-standard link scheme: {u}")
    expected_link_hosts = ["linkedin.com/in/shabaz17", "github.com/MdShabazS"]
    for host in expected_link_hosts:
        if not any(host.lower() in u.lower() for u in links):
            errors.append(f"expected hyperlink missing: {host}")

    # ---- Formatting hazards
    if pages != 1:
        errors.append(f"resume is {pages} pages (target 1)")
    if len(text.strip()) < 1200:
        errors.append("insufficient extractable text (possible image-only PDF)")
    bad_pct = re.findall(r"\d{1,3}\.\d%", text)
    if bad_pct:
        errors.append(f"precise (possibly fabricated) percentages: {bad_pct}")

    # ---- Repetitive action verbs (writing quality)
    verbs = re.findall(r"(?m)^\s*[•·]\s*([A-Z][a-z]+)", text)  # bullet-leading verbs
    from collections import Counter
    vc = Counter(verbs)
    repeated = {v: n for v, n in vc.items() if n > 2}
    if repeated:
        warns.append(f"action verb used >2x: {repeated}")

    # ---- Quantified-bullet ratio (impact)
    bullets = re.findall(r"(?m)^\s*[•·]\s*(.+)$", text)
    quant = [b for b in bullets if re.search(r"\d", b)]
    qratio = (len(quant) / len(bullets)) if bullets else 0

    # ================= readiness score =================
    score, rep = 0.0, []

    pz = (10 if pages == 1 else 0) + (5 if len(text.strip()) > 1200 else 0) + (5 if len(links) >= 3 else 0)
    rep.append(("Parseability", pz, 20, f"pages={pages}, chars={len(text.strip())}, links={len(links)}")); score += pz

    cz = sum(2 for k in ("name", "email", "phone", "linkedin_link", "github_link") if checks[k])
    rep.append(("Contact & links", cz, 10, "all present" if cz == 10 else "gaps")); score += cz

    sz = 15 * len(found_sections) / len(SECTIONS)
    rep.append(("Standard sections", round(sz, 1), 15, f"{len(found_sections)}/{len(SECTIONS)}")); score += sz

    fracs, per_role = [], {}
    for role, kws in ROLE_KEYWORDS.items():
        present = [k for k in kws if k.lower() in flat]
        fracs.append(len(present) / len(kws))
        per_role[role] = (len(present), len(kws), sorted(set(kws) - set(present)))
    kz = 25 * (sum(fracs) / len(fracs))
    rep.append(("Keyword coverage", round(kz, 1), 25,
                " | ".join(f"{r.split()[0]}:{per_role[r][0]}/{per_role[r][1]}" for r in per_role))); score += kz

    ez = 10 * len([t for t in EVIDENCE_TOKENS if t.lower() in flat]) / len(EVIDENCE_TOKENS)
    rep.append(("Evidence & specificity", round(ez, 1), 10,
                f"{len([t for t in EVIDENCE_TOKENS if t.lower() in flat])}/{len(EVIDENCE_TOKENS)} tokens")); score += ez

    iz = 10 * qratio
    rep.append(("Quantified impact", round(iz, 1), 10, f"{len(quant)}/{len(bullets)} bullets have numbers")); score += iz

    hz = 10.0
    if bad_pct: hz -= 5
    if repeated: hz -= 2
    rep.append(("Hygiene / writing", round(hz, 1), 10, "clean" if hz == 10 else "; ".join(warns))); score += hz

    # ================= output =================
    print("=" * 72)
    print("ATS READINESS (internal, from extracted PDF text) — not a vendor score")
    print("=" * 72)
    for name, got, mx, detail in rep:
        print(f"  {name:<24} {got:>5} / {mx:<3}  {detail}")
    print("-" * 72)
    print(f"  {'TOTAL':<24} {round(score,1):>5} / 100")
    print("-" * 72)
    print(f"Quantified-bullet ratio: {len(quant)}/{len(bullets)} = {qratio*100:.0f}%")
    print("Scored-keyword coverage by role (only genuinely supportable terms are scored):")
    for role, (p, t, gaps) in per_role.items():
        print(f"  {role}: {p}/{t} present" + (f"; missing {gaps}" if gaps else ""))
    print("Advanced learning gaps by role (NOT scored, NOT added as fake skills):")
    for role, gaps in ROLE_GAPS.items():
        print(f"  {role}: {gaps}")

    print("-" * 72)
    print("External-style JD alignment (full JD keyword sets incl. gaps — honest match %):")
    print("  (approximates Jobscan/Resume Worded targeted match; NOT the internal score)")
    def _has(term):
        t = term.lower()
        # match plain forms and common variants
        if t == "arm cortex-m":
            return "cortex-m" in flat
        return t in flat
    for role, kws in JD_ALIGNMENT.items():
        present = [k for k in kws if _has(k)]
        missing = [k for k in kws if not _has(k)]
        pct = 100 * len(present) / len(kws)
        print(f"  {role:<30} {len(present):>2}/{len(kws):<2} = {pct:4.0f}%   missing: {missing}")

    print("-" * 72)
    print("Format / parse checklist:")
    checklist = [
        ("plain-text extraction", len(text.strip()) > 1200),
        ("name extractable", checks["name"]),
        ("email extractable", checks["email"]),
        ("phone extractable", checks["phone"]),
        ("LinkedIn hyperlink", checks["linkedin_link"]),
        ("GitHub hyperlink", checks["github_link"]),
        ("email hyperlink", checks["email_link"]),
        ("all sections detected", len(found_sections) == len(SECTIONS)),
        ("education present", "EDUCATION" in upper and "8.38" in text),
        ("dates present", bool(re.search(r"(19|20)\d\d", text))),
        ("single page", pages == 1),
        ("no removed projects", not any(t.lower() in low for t in REMOVED)),
        ("no future skills as current", not any(t.lower() in skills_block.lower() for t in FUTURE_AS_SKILL)),
        ("no confidentiality wording", "confidential" not in low),
        ("no fabricated precise %", not bad_pct),
        ("no broken/odd links", all(u.startswith(("http", "mailto:")) for u in links)),
    ]
    for label, ok in checklist:
        print(f"  [{'x' if ok else ' '}] {label}")
    print(f"\nPlain-text written: {os.path.relpath(TXT, ROOT)}")

    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        print("\nRESUME VALIDATION: FAIL")
        sys.exit(1)
    print(f"\nRESUME VALIDATION: PASS (readiness {round(score)}/100)")


if __name__ == "__main__":
    main()
