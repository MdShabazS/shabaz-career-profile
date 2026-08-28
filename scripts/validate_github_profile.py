#!/usr/bin/env python3
"""Validate the GitHub profile README (rich card-based, embedded/automotive redesign).

Reads github/profile-readme.md (canonical source; identical content is deployed to
MdShabazS/MdShabazS/README.md) and checks structure, honesty, and consistency with
the finalized resume. This redesign intentionally uses a banner, a controlled set of
technology/credential badges, project cards, and ONE GitHub stats component — so the
validator allows those but flags vanity widgets, keyword walls, and factual drift.

Checks:
  - link format; project links resolve to real repos; no fabricated URLs
  - removed projects / excluded tech absent (NexCast, Pega, YOLO/Ultralytics, ...)
  - future/gap skills not listed as current in the Tech Stack skills block
  - Nokia: present-tense phrase; NO future "16 September 2026" date; no confidentiality
  - AEGIS labelled design/in-progress, never completed
  - one stats component only (no streak/trophy/top-langs/profile-views pileup)
  - badge count sane (not a 30+ wall); banner has alt text
  - balanced HTML tags; no duplicate sections
  - facts consistent with the locked resume

Optional live link check:  python3 scripts/validate_github_profile.py --check-links
Exit 0 = pass, 1 = fail.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "github", "profile-readme.md")

KNOWN_REPOS = {
    "Automotive-Body-Control-Module-ESP32",
    "Smart-Wellness-Desk-Assistant",
    "visionpay",
    "aegis",
    "MdShabazS",
}
# Removed projects + excluded tech + vanity widgets that must never appear.
FORBIDDEN = ["NexCast", "Pega", "Bharatiya", "NIDAR", "YOLO", "Ultralytics", "MineGuard",
             "komarev", "profile views", "profile-view",
             "streak-stats", "github-readme-streak", "github-profile-trophy", "trophy",
             "repos-per-language", "most-commit-language", "top-langs"]
# Future/gap skills — allowed only in the "Learning next" line / "Currently Building",
# never in the Tech Stack skills block.
FUTURE_SKILLS = ["RTOS", "FreeRTOS", "CAN", "LIN", "UDS", "AUTOSAR", "MISRA",
                 "ISO 26262", "ASPICE", "JTAG", "SWD", "DMA", "UART", "SPI", "Linux"]
REMOVED_SKILLS = ["Java", "Firebase", "React", "Node.js", "Flask", "REST API"]


def main():
    check_links = "--check-links" in sys.argv
    if not os.path.exists(README):
        print("README source not found:", README)
        sys.exit(1)
    md = open(README, encoding="utf-8").read()
    low = md.lower()
    errors, warns = [], []

    # ---- Links ----------------------------------------------------------
    md_links = re.findall(r"\]\((.*?)\)", md)
    html_hrefs = re.findall(r'href="(.*?)"', md)
    img_srcs = re.findall(r'<img[^>]*?src="(.*?)"', md)
    nav_links = [u for u in md_links + html_hrefs]

    for u in nav_links:
        if u.startswith("mailto:"):
            continue
        if not u.startswith("https://"):
            errors.append(f"non-https/malformed link: {u}")
        if " " in u.strip():
            errors.append(f"link contains a space (malformed): {u}")

    for u in nav_links:
        m = re.match(r"https://github\.com/MdShabazS/([^/)#\"]+)", u)
        if m and m.group(1) not in KNOWN_REPOS:
            errors.append(f"link points to unknown/possibly-fake repo: {m.group(1)}")

    for host in ["linkedin.com/in/shabaz17", "github.com/MdShabazS",
                 "mailto:md.shabaz.2005@gmail.com"]:
        if host not in md:
            errors.append(f"expected contact link missing: {host}")

    # ---- Banner / images / accessibility --------------------------------
    banner = [s for s in img_srcs if "profile-banner" in s]
    if not banner:
        errors.append("profile banner image not referenced")
    # every <img> should have alt text (accessibility); empty alt="" allowed for decorative
    for tag in re.findall(r"<img[^>]*>", md):
        if "alt=" not in tag:
            warns.append(f"image without alt attribute: {tag[:60]}...")

    # ---- Badge / widget discipline --------------------------------------
    shield_count = len(re.findall(r"img\.shields\.io", md))
    if shield_count > 16:
        errors.append(f"too many shield badges ({shield_count}); looks like a badge wall")
    elif shield_count > 12:
        warns.append(f"{shield_count} shield badges — keep it controlled")

    # exactly one stats/summary component; no vanity pileup
    stat_providers = {
        "profile-summary-cards": len(re.findall(r"github-profile-summary-cards", md)),
        "github-readme-stats": len(re.findall(r"github-readme-stats", md)),
    }
    stat_imgs = re.findall(r"(github-profile-summary-cards|github-readme-stats)[^\"']*", md)
    if len(stat_imgs) > 1:
        # allow a single provider used once; more than one stat image = pileup
        errors.append(f"more than one GitHub stats component present ({len(stat_imgs)}) — keep exactly one")

    # ---- Forbidden content ----------------------------------------------
    for term in FORBIDDEN:
        if term.lower() in low:
            errors.append(f"forbidden term present: {term}")

    # ---- Tech Stack skills block: no future/removed skills as current ---
    def between(start_pat, end_pat):
        m = re.search(start_pat + r"(.*?)" + end_pat, md, re.S | re.I)
        return m.group(1) if m else ""
    # skills block = under '## Tech Stack' up to the 'Learning next' sub line
    skills_block = between(r"##\s*Tech Stack", r"Learning next")
    if not skills_block:
        skills_block = between(r"##\s*Tech Stack", r"\n---")
    if not skills_block.strip():
        errors.append("Tech Stack skills block not found")

    for sk in FUTURE_SKILLS:
        if re.search(rf"(?<![A-Za-z]){re.escape(sk)}(?![A-Za-z])", skills_block):
            errors.append(f"future/gap skill '{sk}' listed as current in Tech Stack")
    for sk in REMOVED_SKILLS:
        if sk.lower() in skills_block.lower():
            errors.append(f"removed skill '{sk}' listed as current in Tech Stack")

    # ---- Nokia rules ----------------------------------------------------
    if "16 September 2026" in md or "16 september 2026" in low:
        errors.append("future Nokia start date '16 September 2026' shown (should be omitted)")
    if "currently working as a student intern at nokia" not in low:
        errors.append("required Nokia phrasing missing: 'Currently working as a Student Intern at Nokia.'")
    if "confidential" in low:
        errors.append("confidentiality wording present for Nokia (must be removed)")

    # ---- AEGIS must be labelled planned/in-progress ---------------------
    if "aegis" in low:
        i = low.index("aegis")
        ctx = low[i:i + 260]
        if not any(w in ctx for w in ["design", "in-progress", "in progress", "not yet built", "currently building", "planned"]):
            errors.append("AEGIS present but not clearly labelled design/in-progress")

    # ---- Duplicate sections ---------------------------------------------
    headings = re.findall(r"(?m)^#{1,6}\s+(.*)$", md)
    seen, dups = set(), set()
    for h in headings:
        k = re.sub(r"[^\w ]", "", h).strip().lower()
        if k in seen:
            dups.add(k)
        seen.add(k)
    if dups:
        errors.append(f"duplicate section headings: {sorted(dups)}")

    # ---- Balanced HTML tags ---------------------------------------------
    for tag in ["table", "tr", "td", "ul", "h3", "p"]:
        open_ct = len(re.findall(rf"<{tag}[ >]", md))
        close_ct = len(re.findall(rf"</{tag}>", md))
        if open_ct != close_ct:
            errors.append(f"unbalanced <{tag}> tags ({open_ct} open / {close_ct} close)")

    # ---- Facts / consistency with locked resume -------------------------
    facts = {
        "name 'Mohammed Shabaz S'": "Mohammed Shabaz S" in md,
        "headline Embedded|Automotive": "Embedded Engineer" in md and "Automotive Embedded Systems" in md,
        "CGPA 8.38": "8.38" in md,
        "Expected 2027": "2027" in md,
        "iHelp present": "iHelp Robotics" in md,
        "MITRA named": "MITRA" in md,
        "BITM": "BITM" in md,
        "ARM Cortex-M4": "Cortex-M4" in md,
        "featured: Automotive BCM": "Automotive Body Control Module" in md,
        "featured: Smart Wellness": "Smart Wellness Desk Assistant" in md,
        "featured: VisionPay": "VisionPay" in md,
    }
    for k, v in facts.items():
        if not v:
            errors.append(f"fact/consistency '{k}' missing or wrong")

    # ---- Optional live link check ---------------------------------------
    if check_links:
        import urllib.request
        to_check = sorted(set(u for u in nav_links if u.startswith("https://github.com")))
        for u in to_check:
            try:
                req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
                code = urllib.request.urlopen(req, timeout=8).status
                print(f"  [live] {code}  {u}")
                if code >= 400:
                    errors.append(f"live link {u} -> HTTP {code}")
            except Exception as e:
                warns.append(f"live link check failed (network?) for {u}: {e}")

    # ================= output =================
    print("=" * 72)
    print("GITHUB PROFILE README VALIDATION (rich redesign)")
    print("=" * 72)
    print(f"file: {os.path.relpath(README, ROOT)}")
    print(f"links: {len(nav_links)} | images: {len(img_srcs)} | shields: {shield_count} | "
          f"stat-cards: {len(stat_imgs)} | headings: {len(headings)}")
    print("sections:", ", ".join(h for h in headings if h.strip()))
    print("-" * 72)
    checklist = [
        ("banner present with alt text", bool(banner) and all("alt=" in t for t in re.findall(r"<img[^>]*profile-banner[^>]*>", md))),
        ("controlled badge count (<=16)", shield_count <= 16),
        ("exactly one stats component", len(stat_imgs) <= 1),
        ("no vanity widgets (streak/trophy/views/langs)", not any(t in low for t in ["komarev", "streak", "trophy", "repos-per-language", "most-commit-language", "top-langs"])),
        ("no removed projects / excluded tech", not any(t.lower() in low for t in FORBIDDEN)),
        ("no future skills as current (Tech Stack)", not any(re.search(rf"(?<![A-Za-z]){re.escape(sk)}(?![A-Za-z])", skills_block) for sk in FUTURE_SKILLS)),
        ("no removed skills as current (Tech Stack)", not any(sk.lower() in skills_block.lower() for sk in REMOVED_SKILLS)),
        ("project links resolve to real repos", not any("unknown/possibly-fake" in e for e in errors)),
        ("contact links present", all(h in md for h in ["linkedin.com/in/shabaz17", "github.com/MdShabazS", "mailto:md.shabaz.2005@gmail.com"])),
        ("Nokia present-tense, no future date", "16 September 2026" not in md and "currently working as a student intern at nokia" in low),
        ("no Nokia confidentiality wording", "confidential" not in low),
        ("AEGIS labelled design/in-progress", not any("AEGIS present but not clearly" in e for e in errors)),
        ("3 featured projects present", facts["featured: Automotive BCM"] and facts["featured: Smart Wellness"] and facts["featured: VisionPay"]),
        ("no duplicate sections", not dups),
        ("balanced HTML tags", not any("unbalanced" in e for e in errors)),
        ("facts consistent (name/headline/CGPA/Cortex-M4)", facts["name 'Mohammed Shabaz S'"] and facts["headline Embedded|Automotive"] and facts["CGPA 8.38"] and facts["ARM Cortex-M4"]),
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
