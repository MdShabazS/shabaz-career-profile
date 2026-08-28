# GitHub Profile README Research (2026) — Embedded / Automotive Focus

Research behind the redesigned `github.com/MdShabazS` profile README. Primary positioning: **Embedded Engineer | Automotive Embedded Systems**; secondary: Software Engineering; supporting: AI/ML & Computer Vision. Format per finding: **SOURCE → FINDING → WHY IT MATTERS → APPLICATION TO MY PROFILE.** Labels kept separate:

- `USER FACT` — verified fact about Mohammed Shabaz S (career-profile repo / user confirmation).
- `RESEARCH` — external market/recruiter finding. Never becomes a fact about Shabaz.
- `RECOMMENDATION` — a README decision derived from the two.

Accessed **2026-08-28**. The profile README is `MdShabazS/MdShabazS/README.md` (special self-named repo, branch `main`) — the file that renders on the profile page.

---

## 0. Audit of the current profile README (what it does wrong)

`USER FACT` — the live `MdShabazS/MdShabazS/README.md` today is **software-first and decoration-heavy**, and contradicts the current source of truth:
- Positions "Primary Track: Software Engineer / Software Developer" — should now be **Embedded / Automotive first**.
- Badge/vanity load: image banner, `for-the-badge` shields, a **profile-views counter (komarev)**, and a **skillicons wall** listing `react, nodejs, flask, firebase` — none are current verified skills.
- Lists **YOLO / Ultralytics exposure** — explicitly `EXCLUDED` in the source of truth (tied to the excluded drone/NIDAR work).
- Skill badges claim "Java – Learning", "REST APIs", "C – Intermediate" — inconsistent with the finalized resume (Java/Firebase removed; levels are Basic; REST is a gap).
- Multi-column HTML `<table>` layout (fixed `width="33%"`) — poor mobile reflow.
- Uses "7th Semester" and other stale framings.

`RECOMMENDATION`: full rebuild — embedded/automotive-first, no badge/vanity walls, no excluded tech, consistent with the locked resume and career-profile repo.

## 1. What recruiters actually look at

- **SOURCE:** Instahyre GitHub Profile Checklist 2026; readmedesign "what recruiters look for"; reskilll "GitHub profile that gets you hired 2026".
  - `RESEARCH`: Recruiters spend ~30 seconds. They look at **pinned repositories, the profile README, recent activity, and the contribution graph** — not badge counts. Quality of 2–4 polished repos beats a wall of half-finished ones. "Clear, specific, and linked beats flashy."
  - **WHY IT MATTERS:** The README's job is to route a skimming recruiter to real, relevant work fast and truthfully.
  - `RECOMMENDATION`: Lead with a one-line positioning statement, then a tight **Featured Projects** block (3 strong repos with one-line problem + stack + evidence + link). Keep total length short enough to skim on one screen.

## 2. Structure / section order

- **SOURCE:** Quillly "README examples 2026: what works"; codeboards.io README guide 2026; Markdown Studios README guide.
  - `RESEARCH`: Effective order = **one-line positioning → focused profile card/stats → featured projects → current work → writing/case studies → contact.** Identity line pattern: "I build [type of system] for [audience/problem], mostly with [stack]."
  - `RECOMMENDATION`: Order = **Header (name + headline) → About (identity + focus bullets) → Experience (compact) → Featured Projects → Currently Working On → Technical Skills → Education & Leadership → Contact.** Experience is placed high because real named internships (Nokia, iHelp) are strong credibility for a student; Featured Projects immediately follow because they carry the embedded evidence.

## 3. Badges — signal vs noise

- **SOURCE:** readmedesign; reskilll; Instahyre 2026 — all consistent.
  - `RESEARCH`: "Walls of badges that look impressive but say nothing" are skimmed past. Recruiters want signal, not noise. Animated GIFs distract from the work.
  - **WHY IT MATTERS:** Badge walls cost vertical space and credibility while adding no information; broken shield images look unmaintained.
  - `RECOMMENDATION`: **No badge wall.** Use clean, categorized **text** skill lists (accessible, mobile-safe, never broken). No `for-the-badge` shields, no skillicons grid. A recruiter reads real skills in words, not logos.

## 4. Stats / widgets — vanity check

- **SOURCE:** Instahyre 2026; DEV "top GitHub profile tools and stats generators 2026" (directional); reskilll.
  - `RESEARCH`: Recruiters read the **native contribution graph** directly; third-party stat cards (github-readme-stats, streak, top-languages, trophies, profile-views) are widely treated as **vanity** and can misrepresent (top-languages skews to repo file sizes, e.g. a notebook inflates "Jupyter"). "Recruiters don't count green squares."
  - `RECOMMENDATION`: **Omit all stat widgets** (no stats card, streak, trophies, top-languages, profile-views). Zero vanity components. This is the honest, higher-signal choice for a Tier-1 engineering profile.

## 5. Featured projects — how to present

- **SOURCE:** Quillly; reskilll; readmedesign 2026.
  - `RESEARCH`: For each pinned/featured project: **one-line description of what it does and for whom**, the stack, a couple of evidence points (metrics / engineering decisions), and a link. A screenshot/live demo helps most; text walls hurt.
  - `RECOMMENDATION`: Feature exactly **3** completed, relevant repos with clean READMEs — **Automotive BCM, Smart Wellness Desk Assistant, VisionPay** — each as: bold name → one-line problem → `Stack:` line → 1–2 evidence bullets → repo link. No fabricated demo links (none of the repos deploy a live demo). AEGIS goes under *Currently working on* (planned), not Featured. MITRA stays under Experience (company product; not linked, per the confidentiality boundary in the source of truth). Excluded repos (NexCast, drone/NIDAR/YOLO, MineGuard, etc.) are never featured.

## 6. Mobile & accessibility

- **SOURCE:** codeboards.io; Markdown Studios; general GitHub rendering behaviour.
  - `RESEARCH`: A large share of profile views are on mobile. Multi-column HTML `<table>` layouts with fixed widths do **not** reflow — they force horizontal scroll or squash text. Markdown headings/lists reflow cleanly. Alt text on any image aids accessibility.
  - `RECOMMENDATION`: Single-column, markdown-based layout. **No layout tables.** Centered header via minimal `<h1>/<p align="center">` only. No banner image (keeps it light and unbreakable). Everything readable top-to-bottom on a phone.

## 7. Honesty / consistency with the locked resume

- `USER FACT`: The finalized resume is locked (Embedded/Automotive-first; skills = verified, bullet-backed set; automotive standards and RTOS/UART/SPI/CAN are learning gaps; Nokia is high-level with no confidentiality wording).
  - `RECOMMENDATION`: The README may add *more* detail than the resume but must not introduce new skills, titles, projects, achievements, or metrics. Future skills (UART/SPI/RTOS/CAN) appear only in an explicit **"Learning next"** line, never as current skills. Nokia: "Currently a Student Intern at Nokia" — no project detail, no confidentiality mention, no invented responsibilities.

---

## 8. Project images / screenshots (the centerpiece)

- **SOURCE:** pushpen.dev "README best practices 2026"; UniLink README templates 2026; Quillly 2026.
  - `RESEARCH`: "A screenshot or short GIF of the tool in action is almost always worth more than another badge." Visuals should support a message, not fill space — "pick one source, one card, and let the README breathe." For every featured repo, write one sentence a non-developer understands.
  - **WHY IT MATTERS:** Real project imagery is the single strongest "this person actually builds things" signal — far stronger than text cards, which read like a resume.
  - `RECOMMENDATION`: Make Featured Projects the visual centerpiece with **real project imagery**: the Automotive BCM uses the actual breadboard build photo (`images/hardware_setup.jpg` from the repo); Smart Wellness uses its real wiring diagram (`Media/Wiring_Diagram.png`); VisionPay has no repo image, so a **clean designed thumbnail** in the same visual language is used (labelled by content, not a fake screenshot). Each card = full-width image + one-line summary + 2 highlights + stack + repo link. Consistent 820×440 dark cards with a tag, title, stack line and accent bar.

## 9. Image hosting, light/dark & accessibility

- **SOURCE:** GitHub docs (supported HTML/images); codeboards / Markdown Studios 2026; general camo/proxy behaviour.
  - `RESEARCH`: GitHub proxies external images (camo) and strips `<style>`/scripts/most CSS; there are **no media queries** in README, so true responsive stacking is impossible — multi-column HTML tables squish on mobile rather than stacking. Repo-hosted assets are more reliable than fragile third-party widgets. Readers use light or dark GitHub themes.
  - `RECOMMENDATION`: Host the banner and project thumbnails **in the repo** (`assets/`), not on external services, so they never break. The cards are self-contained **dark** images with their own background, so they read as intentional "cards" in both light and dark GitHub themes (no `<picture>`/theme-swap needed). Body text/tables use GitHub's own theme colours and adapt automatically. Every image carries alt text. Because media queries aren't available, keep table cell text short so the unavoidable mobile squish stays readable; the full-width image cards (the centerpiece) reflow perfectly on mobile.

## 10. OLD → CURRENT → TARGET comparison

| Aspect | OLD README (badge-heavy, software-first) | CURRENT minimal (before this build) | TARGET (this build) |
|---|---|---|---|
| Positioning | Software-first ("Primary: Software Developer") | Embedded-first (correct) but plain | **Embedded/automotive-first + visually rich** |
| Hero | Banner with software-first baked text | None (plain heading) | **New embedded/automotive banner** (MCU + OFF/ACC/ON motif) |
| Visual identity | Present but noisy (skillicons wall, profile-views, YOLO) | Absent (reads like a document) | **Present and controlled** (cards, one stats card, tech icons) |
| Projects | Text cards; NexCast present | Text bullets | **Image cards with real hardware photo + wiring diagram** |
| Facts | Stale (NexCast/Pega/Java/YOLO) | Correct | Correct + richer, verified evidence |
| Vanity widgets | Many (views/streak/langs/followers) | None | **Exactly one** summary card |
| Mobile | 2–3 col tables squish; ok | Perfect (plain) | Image cards reflow; tables squish (accepted, GitHub limit) |

**Kept from OLD:** banner concept, credential/contact badges, snapshot table, 3-column focus, technology icons, project cards, one activity component, footer. **Removed from OLD:** software-first framing, NexCast/Pega/Java/YOLO, profile-views counter, multi-widget stat pileup. **Improved:** real project images, embedded/automotive banner, honest present-tense Nokia, controlled badge/widget count.

### Sources (accessed 2026-08-28)
- [Instahyre — GitHub Profile Checklist 2026: what recruiters actually look at](https://resources.instahyre.com/blog/github-profile-checklist/)
- [readmedesign — what tech recruiters actually look for in a GitHub profile](https://readmedesign.com/blog/what-recruiters-look-for)
- [reskilll — GitHub profile that gets you hired: 2026 guide](https://reskilll.com/blogs/github-profile-gets-you-hired-2026-developer-portfolio-guide/)
- [Quillly / devbio — GitHub profile README examples 2026: what works](https://devbio.me/blogs/github-profile-readme-examples-2026)
- [codeboards.io — GitHub profile README guide 2026](https://codeboards.io/blog/github-profile-readme-guide)
- [Markdown Studios — standout GitHub profile README in 2026](https://www.markdownstudios.com/blog/github-profile-readme-guide)
- [DEV — top GitHub profile tools and stats generators 2026 (directional)](https://dev.to/_d7eb1c1703182e3ce1782/top-github-profile-tools-and-stats-generators-2026-2h3h)
- [pushpen.dev — GitHub README best practices 2026](https://pushpen.dev/blog/github-readme-best-practices-2026)
- [UniLink — GitHub README templates 2026](https://app.unilink.us/blog/github-readme-templates-2026)
- [tandpfun/skill-icons — technology icons for READMEs](https://github.com/tandpfun/skill-icons)
