#!/usr/bin/env python3
"""Validate the GitHub profile README for the embedded/automotive redesign.

Reads github/profile-readme.md (the canonical source; identical content is
deployed to MdShabazS/MdShabazS/README.md) and checks:
  - link format + no fabricated/raw URLs; project links point to real repos
  - duplicate sections; broken markdown / malformed HTML (basic)
  - removed projects, excluded tech, future-skills-as-current leakage
  - date / company / project-name consistency with the locked resume
  - badge / widget / vanity counts (should be ~0)
  - factual consistency (name, headline, CGPA, positioning, no confidentiality)

Optional live link check:  python3 scripts/validate_github_profile.py --check-links
(best-effort HTTP HEAD/GET with timeout; network failure is a warning, not an error)

Exit 0 = pass, 1 = fail.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "github", "profile-readme.md")

# Repos that legitimately exist and may be linked from the profile.
KNOWN_REPOS = {
    "Automotive-Body-Control-Module-ESP32",
    "Smart-Wellness-Desk-Assistant",
    "visionpay",
    "MdShabazS",
}
# Terms that must never appear anywhere (removed projects + excluded tech).
FORBIDDEN = ["NexCast", "Pega", "Bharatiya", "NIDAR", "YOLO", "Ultralytics",
             "MineGuard", "komarev", "profile views", "skillicons"]
# Future/gap skills — allowed ONLY in a learning/currently-working context, never
# in the Technical Skills block.
FUTURE_SKILLS = ["RTOS", "FreeRTOS", "CAN", "LIN", "UDS", "AUTOSAR", "MISRA",
                 "ISO 26262", "ASPICE", "JTAG", "SWD", "DMA", "UART", "SPI", "Linux"]
# Skills removed from the current set (must not be claimed as current skills).
REMOVED_SKILLS = ["Java", "Firebase", "React", "Node.js", "Flask", "REST API"]


def main():
    check_links = "--check-links" in sys.argv
    if not os.path.exists(README):
        print("README source not found:", README)
        sys.exit(1)
    md = open(README, encoding="utf-8").read()
    low = md.lower()
    errors, warns = [], []

    # ---- Links -----------------------------------------------------------
    md_links = re.findall(r"\]\((.*?)\)", md)
    html_links = re.findall(r'href="(.*?)"', md)
    img_srcs = re.findall(r'<img[^>]*src="(.*?)"', md) + re.findall(r"!\[[^\]]*\]\((.*?)\)", md)
    all_links = md_links + html_links

    for u in all_links:
        if u.startswith("mailto:"):
            continue
        if not u.startswith("https://"):
            errors.append(f"non-https or malformed link: {u}")
        if " " in u.strip():
            errors.append(f"link contains a space (malformed): {u}")

    # project/github links must resolve to a KNOWN repo or the profile itself
    for u in all_links:
        m = re.match(r"https://github\.com/MdShabazS/([^/)#]+)", u)
        if m:
            repo = m.group(1)
            if repo not in KNOWN_REPOS:
                errors.append(f"link points to unknown/possibly-fake repo: {repo}")

    # expected contact links present
    for host in ["linkedin.com/in/shabaz17", "github.com/MdShabazS",
                 "mailto:md.shabaz.2005@gmail.com"]:
        if host not in md:
            errors.append(f"expected contact link missing: {host}")

    # no bare long raw URLs shown as visible text (link labels should be clean)
    for m in re.finditer(r"(?<!\()(?<!\")https?://\S{40,}", md):
        warns.append(f"long raw URL visible in text: {m.group(0)[:50]}...")

    # ---- Badges / widgets / vanity --------------------------------------
    badge_count = len(re.findall(r"img\.shields\.io", md))
    if badge_count > 0:
        errors.append(f"shield badges present ({badge_count}); redesign uses none")
    for term in ["github-readme-stats", "streak-stats", "github-profile-trophy",
                 "komarev", "skillicons", "readme-stats"]:
        if term in low:
            errors.append(f"vanity/stat widget present: {term}")
    img_ct = len(img_srcs)
    if img_ct > 0:
        warns.append(f"{img_ct} image(s) present — confirm each is meaningful and has alt text")

    # ---- Forbidden content ----------------------------------------------
    for term in FORBIDDEN:
        if term.lower() in low:
            errors.append(f"forbidden term present: {term}")

    # ---- Section split: skills block vs learning/working block ----------
    # Technical Skills block = from '### Technical Skills' to the next '### '
    def block(header):
        m = re.search(rf"###\s+{re.escape(header)}(.*?)(?=\n###\s|\Z)", md, re.S)
        return m.group(1) if m else ""
    skills_block = block("Technical Skills")
    working_block = block("Currently Working On")
    learn_ok_zone = working_block  # future skills allowed here (+ 'Learning next' bullet in About)

    if not skills_block:
        errors.append("Technical Skills section not found")

    for sk in FUTURE_SKILLS:
        if re.search(rf"(?<![A-Za-z]){re.escape(sk)}(?![A-Za-z])", skills_block):
            errors.append(f"future/gap skill '{sk}' listed in Technical Skills (should be learning-only)")
    for sk in REMOVED_SKILLS:
        if sk.lower() in skills_block.lower():
            errors.append(f"removed skill '{sk}' listed in Technical Skills")

    # ---- Duplicate sections ---------------------------------------------
    headings = re.findall(r"(?m)^#{1,6}\s+(.*)$", md)
    seen, dups = set(), set()
    for h in headings:
        key = h.strip().lower()
        if key in seen:
            dups.add(key)
        seen.add(key)
    if dups:
        errors.append(f"duplicate section headings: {sorted(dups)}")

    # ---- Facts / consistency with locked resume -------------------------
    facts = {
        "name 'Mohammed Shabaz S'": "Mohammed Shabaz S" in md,
        "headline Embedded|Automotive": "Embedded Engineer" in md and "Automotive Embedded Systems" in md,
        "CGPA 8.38": "8.38" in md,
        "Expected 2027": "2027" in md,
        "Nokia present-tense": "Nokia" in md and "Present" in md,
        "Nokia exact date": "16 September 2026" in md,
        "iHelp dates": "23 March" in md and "23 August 2026" in md,
        "MITRA named": "MITRA" in md,
        "BITM": "BITM" in md,
    }
    for k, v in facts.items():
        if not v:
            errors.append(f"fact/consistency '{k}' missing or wrong")

    # Nokia confidentiality wording must NOT appear (latest instruction)
    if "confidential" in low:
        errors.append("confidentiality wording present for Nokia (must be removed)")

    # AEGIS must be labelled in-progress/planned, never completed
    if "aegis" in low:
        aegis_ctx = low[low.index("aegis"): low.index("aegis") + 240]
        if not any(w in aegis_ctx for w in ["design", "early", "planned", "in progress", "not yet built"]):
            errors.append("AEGIS present but not clearly labelled design/planned")

    # ---- Basic markdown / HTML sanity -----------------------------------
    if md.count("](") != md.count(")") - md.count(") ") - 0 and md_links and False:
        pass  # (intentionally skipped: naive bracket counting is unreliable)
    # balanced common HTML tags used here
    for tag in ["h1", "p"]:
        if md.count(f"<{tag}") != md.count(f"</{tag}>"):
            errors.append(f"unbalanced <{tag}> tags")
    # no layout tables (mobile)
    if "<table" in low:
        warns.append("HTML <table> present — verify mobile reflow (redesign avoids layout tables)")

    # ---- Optional live link check ---------------------------------------
    if check_links:
        import urllib.request
        for u in sorted(set(u for u in all_links if u.startswith("https://"))):
            try:
                req = urllib.request.Request(u, method="HEAD",
                                             headers={"User-Agent": "Mozilla/5.0"})
                code = urllib.request.urlopen(req, timeout=8).status
                if code >= 400:
                    errors.append(f"live link {u} -> HTTP {code}")
                else:
                    print(f"  [live] {code}  {u}")
            except Exception as e:
                warns.append(f"live link check failed (network?) for {u}: {e}")

    # ================= output =================
    print("=" * 72)
    print("GITHUB PROFILE README VALIDATION")
    print("=" * 72)
    print(f"file: {os.path.relpath(README, ROOT)}")
    print(f"links: {len(all_links)}  | images: {img_ct}  | shield-badges: {badge_count}  | headings: {len(headings)}")
    print("sections:", ", ".join(h for h in headings if h.strip()))
    print("-" * 72)

    checklist = [
        ("no shield/badge wall", badge_count == 0),
        ("no vanity/stat widgets", not any(t in low for t in ["komarev", "github-readme-stats", "streak", "trophy", "skillicons"])),
        ("no forbidden/excluded terms", not any(t.lower() in low for t in FORBIDDEN)),
        ("no future skills in Skills block", not any(re.search(rf"(?<![A-Za-z]){re.escape(sk)}(?![A-Za-z])", skills_block) for sk in FUTURE_SKILLS)),
        ("no removed skills in Skills block", not any(sk.lower() in skills_block.lower() for sk in REMOVED_SKILLS)),
        ("project links resolve to real repos", not any("unknown/possibly-fake repo" in e for e in errors)),
        ("contact links present", all(h in md for h in ["linkedin.com/in/shabaz17", "github.com/MdShabazS", "mailto:md.shabaz.2005@gmail.com"])),
        ("no duplicate sections", not dups),
        ("name/headline/CGPA correct", facts["name 'Mohammed Shabaz S'"] and facts["headline Embedded|Automotive"] and facts["CGPA 8.38"]),
        ("dates consistent", facts["Nokia exact date"] and facts["iHelp dates"]),
        ("no Nokia confidentiality wording", "confidential" not in low),
        ("AEGIS labelled planned/in-progress", not any("AEGIS present but not clearly" in e for e in errors)),
        ("balanced HTML tags", not any("unbalanced" in e for e in errors)),
    ]
    for label, ok in checklist:
        print(f"  [{'x' if ok else ' '}] {label}")

    if warns:
        print("\nWARNINGS:")
        for w in warns:
            print(f"  - {w}")
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        print("\nPROFILE VALIDATION: FAIL")
        sys.exit(1)
    print("\nPROFILE VALIDATION: PASS")


if __name__ == "__main__":
    main()
