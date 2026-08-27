#!/usr/bin/env python3
"""Validate the career profile repository as a single source of truth.

Checks: broken internal links, name spelling, location rule, CGPA certainty,
removed/forbidden facts in current files, future-skills leaking into current
skills, confidentiality/secret leaks, and Nokia date representation.

Run: python3 scripts/validate.py   (exit 0 = pass, 1 = fail)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []
WARN = []

# Files where historical/meta mentions of removed items are allowed.
HIST_ALLOW = ("archive/", "governance/CHANGELOG.md", "scripts/", "AUDIT_REPORT.md")

# A line that documents a removal/exclusion/rule is allowed to name a removed item.
CONTEXT_OK = ("remov", "exclud", "not include", "do not", "don't", "no public",
              "historical", "archive", "absent", "must not", "instead of", "outdated")


def rel(p):
    return os.path.relpath(p, ROOT)


def md_files():
    for dirpath, dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def all_text_files():
    for dirpath, dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for f in files:
            yield os.path.join(dirpath, f)


def read(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


# 1. Broken internal markdown links
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for f in md_files():
    base = os.path.dirname(f)
    for target in link_re.findall(read(f)):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        if not os.path.exists(os.path.join(base, clean)):
            ERRORS.append(f"Broken link in {rel(f)} -> {target}")

# 2. Name spelling: flag misspellings (allow inside an explicit do-not rule)
name_bad = re.compile(r"\bMoh?am[e]?ad\b|\bMohamed\b", re.I)
for f in md_files():
    for i, line in enumerate(read(f).splitlines(), 1):
        if name_bad.search(line) and "not \"Mohammad\"" not in line and "Do not vary" not in line:
            ERRORS.append(f"Possible name misspelling in {rel(f)}:{i}: {line.strip()[:80]}")

# 3. Location rule: identity + PROFILE must assert Ballari, not Bangalore as home
for key in ("profile/identity.md", "PROFILE.md"):
    txt = read(os.path.join(ROOT, key))
    if "Ballari, Karnataka, India" not in txt:
        ERRORS.append(f"{key} must state 'Ballari, Karnataka, India' as location")
    # flag only a location field whose VALUE is Bangalore (Bangalore immediately after 'Location')
    if re.search(r"(?i)Location\**\s*[:|]\s*\**\s*Bangalore", txt):
        ERRORS.append(f"{key} appears to use Bangalore as the profile location")

# 4. CGPA must be current/verified, not uncertain (skip historical/meta files)
for f in md_files():
    r = rel(f)
    if any(r.startswith(h) or r == h for h in HIST_ALLOW):
        continue
    if re.search(r"CGPA[^\n]*(may change|TO_VERIFY|uncertain)", read(f), re.I):
        ERRORS.append(f"CGPA uncertainty language present in {r}")
if "8.38" not in read(os.path.join(ROOT, "profile/education.md")):
    ERRORS.append("profile/education.md missing CGPA 8.38")

# 5. Removed items must not appear as current facts (documented removals allowed)
removed = ["Pega", "NexCast", "Bharatiya Antariksh"]
for f in md_files():
    r = rel(f)
    if any(r.startswith(h) or r == h for h in HIST_ALLOW):
        continue
    for i, line in enumerate(read(f).splitlines(), 1):
        low = line.lower()
        if any(ctx in low for ctx in CONTEXT_OK):
            continue
        for term in removed:
            if term.lower() in low:
                ERRORS.append(f"Removed item '{term}' as current fact in {r}:{i}")

# 6. Future skills must not appear as current skills in current-skills.md
cs = read(os.path.join(ROOT, "skills/current-skills.md"))
current_part = cs.split("## Not current", 1)[0]
future_terms = ["RTOS", "FreeRTOS", "Linux", "AUTOSAR", "MISRA", "ISO 26262",
                "ASPICE", "Docker", "System Design", " CAN", " LIN", "UDS"]
for term in future_terms:
    if term.strip().lower() in current_part.lower():
        ERRORS.append(f"Future skill '{term.strip()}' listed as current in current-skills.md")
# Individual boards must not be bulleted in current-skills (use Microcontrollers)
for board in ["ESP32", "STM32", "Arduino", "Raspberry Pi"]:
    if re.search(rf"(?mi)^- {re.escape(board)}\b", current_part):
        ERRORS.append(f"Board '{board}' bulleted in current-skills; use 'Microcontrollers'")
if "Microcontrollers" not in current_part:
    ERRORS.append("current-skills.md embedded section must list 'Microcontrollers'")

# 7. Nokia representation: Present, no fixed old end date
nk = read(os.path.join(ROOT, "experience/nokia.md"))
if "Present" not in nk:
    ERRORS.append("experience/nokia.md must show Nokia as 'Present'")
if re.search(r"14 Aug(ust)? 2027", nk):
    ERRORS.append("experience/nokia.md still contains the old fixed end date")

# 8. Required project files exactly (6) and NexCast absent
proj_dir = os.path.join(ROOT, "projects")
expected_projects = {"aegis.md", "mitra.md", "visionpay.md", "automotive-bcm.md",
                     "smart-wellness-desk-assistant.md", "skin-disease-classification.md"}
present = {f for f in os.listdir(proj_dir) if f.endswith(".md")
           and f not in ("README.md", "EXCLUDED.md")}
if present != expected_projects:
    ERRORS.append(f"Project files mismatch. Expected {sorted(expected_projects)}, got {sorted(present)}")

# 9. Leadership must contain exactly the three roles
ld = read(os.path.join(ROOT, "leadership/leadership.md"))
for role in ["IEEE CAS Society", "BITM Robotics Club", "Google Student Ambassador"]:
    if role not in ld:
        ERRORS.append(f"leadership.md missing '{role}'")
# AEGIS must not appear as a leadership table row (a prose rule mentioning it is fine)
for line in ld.splitlines():
    if line.lstrip().startswith("|") and "AEGIS" in line:
        ERRORS.append("leadership.md lists AEGIS as a leadership row")

# 10. Secret scan across all files
secret_res = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "OpenAI key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "AWS key": re.compile(r"AKIA[0-9A-Z]{16}"),
}
for f in all_text_files():
    try:
        content = read(f)
    except Exception:
        continue
    if "\x00" in content:
        continue
    for label, pat in secret_res.items():
        if pat.search(content):
            ERRORS.append(f"Possible {label} in {rel(f)}")

if ERRORS:
    print("VALIDATION FAILED:")
    for e in ERRORS:
        print(f"  - {e}")
    if WARN:
        print("Warnings:")
        for w in WARN:
            print(f"  - {w}")
    sys.exit(1)

print("Validation passed.")
print(f"  Markdown files checked: {sum(1 for _ in md_files())}")
print(f"  Projects: {sorted(present)}")
if WARN:
    print("Warnings:")
    for w in WARN:
        print(f"  - {w}")
