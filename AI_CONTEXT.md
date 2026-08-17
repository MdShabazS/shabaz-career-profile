# AI Context: Shabaz Career Profile

This is the first file any AI system should read. The repository is Mohammed Shabaz S's private career intelligence repository and single source of truth.

Use it to answer career questions, generate resumes, prepare for BITM placements, explain projects, identify gaps, and support career decisions. Do not use it as a creative biography.

## Non-Negotiable Rules

- Never invent facts.
- Never exaggerate project ownership.
- Never convert `PLANNED`, `TO_VERIFY`, or `EXCLUDED` facts into `VERIFIED` claims.
- Never claim unsupported technologies, metrics, dates, awards, certifications, rankings, responsibilities, production usage, model architectures, deployment details, team sizes, or company names.
- If a missing metric would improve a resume, write `Metric not currently verified` or omit the metric.
- Use `UNKNOWN`, `NOT_PROVIDED`, or `TO_VERIFY` when information is not available.

## Fact Status System

| Status | Meaning |
|---|---|
| `VERIFIED` | Explicitly supplied by Shabaz or supported by provided evidence |
| `PLANNED` | Intended future work, not completed |
| `TO_VERIFY` | Mentioned but insufficiently confirmed |
| `EXCLUDED` | Explicitly excluded from primary profile/resumes |

Use these fields consistently:

- `fact_status`: whether the fact itself is confirmed.
- `lifecycle_status`: the project or initiative state, such as `COMPLETED`, `ARCHITECTURE_DESIGN`, or `DEMO_LEVEL_COMPLETED`.
- `evidence_status`: whether supporting artifacts are attached in the repository.

If Shabaz confirmed a fact but no supporting artifact is attached, keep `fact_status: VERIFIED` and set `evidence_status: TO_VERIFY`.

## Canonical Source Hierarchy

- Project `facts.yaml`: canonical structured project facts.
- Project `README.md`: human-readable project explanation.
- `AI_CONTEXT.md`: high-level AI context and policy.
- `docs/SOURCE_INDEX.md`: evidence/source map.

When these files overlap, do not invent a reconciliation. Prefer the canonical structured source, then flag any contradiction for review.

## Identity

- Full name: Mohammed Shabaz S
- Professional short name: Shabaz
- Current role context: B.E. ECE student preparing for placements
- Private contact details: `NOT_PROVIDED` in this repository baseline

Canonical files:

- [`profile/personal.yaml`](profile/personal.yaml)
- [`profile/education.yaml`](profile/education.yaml)
- [`profile/languages.yaml`](profile/languages.yaml)
- [`profile/career-goals.yaml`](profile/career-goals.yaml)

Languages are confirmed by Shabaz, but proficiency levels are not yet verified.

## Education

- Degree: B.E. in Electronics and Communication Engineering (ECE)
- Institution: Ballari Institute of Technology and Management (BITM), Bellary
- Current semester: 7th Semester
- Expected graduation: 2027
- CGPA: 8.38
- Class 12: 480 / 600, 80%
- Class 10: 543 marks, 86.88%

## Career Direction

Target roles:

1. Software Engineer / Software Developer
2. Embedded Engineer

Both role directions matter. For BITM placement strategy, software preparation receives higher priority because Shabaz expects more software companies to visit BITM. Embedded remains a parallel opportunity.

AI/ML is an exploration area with project-level exposure. Do not present AI/ML as a finalized specialization or primary target role yet.

## Placement Strategy

Primary preparation areas:

- Java
- DSA
- SQL
- DBMS
- Operating Systems
- Computer Networks
- Aptitude
- Coding rounds
- Communication and interviews
- Git/GitHub
- Project explanation

When a company is announced:

1. Read the company/JD supplied by Shabaz.
2. Extract requirements, eligibility, and selection process.
3. Map requirements to verified profile facts.
4. Identify gaps without inventing coverage.
5. Build a study plan, coding/aptitude plan, technical interview plan, and HR/interview plan.
6. Generate a tailored resume using only verified and relevant facts.

## Skill Truth

Programming:

- C: Intermediate
- C++: Intermediate
- Embedded C: Intermediate
- Python: Intermediate
- Java: Beginner, actively learning for DSA and placements
- SQL: Beginner

Fundamentals:

- DSA: Beginner, actively learning
- DBMS: Beginner, currently learning
- Operating Systems: Beginner, currently learning
- Computer Networks: not learned properly yet
- Aptitude: Beginner, fundamentals started
- English/interview communication: Beginner, significant improvement needed

Hands-on exposure:

- Git / GitHub
- Android Studio
- REST APIs
- OpenCV
- TensorFlow Lite
- STM32CubeIDE / STM32 HAL
- Arduino IDE
- ESP32
- Firebase Realtime Database
- React
- Node.js
- YOLO / Ultralytics

Do not assign proficiency levels to hands-on technologies unless a proficiency level is explicitly verified.

Important hands-on boundaries:

- React and Node.js were used hands-on; exact project association is not currently remembered.
- YOLO / Ultralytics hands-on exposure is confirmed; exact project association is not currently remembered. Do not associate YOLO with NIDAR.
- Firebase Realtime Database is confirmed. Other Firebase services are not remembered.

## Certifications

Completed:

- Python certification
- Embedded Systems training/certificate
- Google Cloud Generative AI Virtual Internship

Planned, not completed:

- Data Structures & Algorithms
- Core Java with AI
- SQL for Data Analytics with AI
- Git & GitHub
- Machine Learning with AI
- Software Testing
- Cloud Computing with AWS
- Generative AI

Never call planned courses completed certifications.

## Experience And Programs

### iHelp Robotics Private Limited

Status: internship, remote.

Project: MITRA.

Confirmed contribution:

- Android app development
- app feature development/improvements
- RTSP stream handling
- phone-camera fallback
- testing/QA
- navigation module
- TTS
- voice interaction/wake-word related app functionality
- app controls/OCR/background behavior where applicable

Boundary: backend/model development belonged to another team. Do not claim Shabaz trained or developed MITRA backend/AI models unless explicitly confirmed later.

### IEEE EMBS Pune Section

Status: completed one-month internship.

Project: Skin Disease Classification.

Team size: 3.

Personal contribution:

- model selection
- model training
- model evaluation
- Python coding
- image processing
- UI/application work
- testing

Boundary: demo-level project. Exact model is not remembered. Do not represent it as productized.

### NexCast Pro Internship

Status: internship project.

Ownership: Shabaz explicitly stated he did it alone.

Known stack and capabilities are documented in [`projects/NexCast-Pro/`](projects/NexCast-Pro/). Do not add capabilities beyond supplied project documentation.

### Pega National Internship Program

Status: currently participating.

Duration: 5 months.

Learning format:

- odd days: sessions
- even days: self-paced learning

## Leadership And Memberships

Leadership:

- BITM Robotics Club: Treasurer
- IEEE CAS Society, IEEE Student Branch BITM: Vice-Chair; previous position Treasurer
- AEGIS: Team Lead; original idea
- Google Student Ambassador: Student Ambassador, 2025

Memberships:

- IEEE member for approximately 4 years
- IEEE Aerospace and Electronic Systems Society (AESS) member

## Project Priority

Use this exact portfolio priority:

1. AEGIS — Team Lead / original idea
2. MITRA — Internship
3. Skin Disease Classification — IEEE Pune internship
4. NexCast Pro — Internship
5. VisionPay — Personal / individual project
6. Automotive BCM — Personal / individual project
7. Smart Wellness Desk Assistant — College team project

Do not reorder without explicit user confirmation.

## AEGIS Architecture Lock

AEGIS is the highest-priority project.

Current status:

- Team project
- Team size: 3
- Shabaz: Team Lead
- Idea: Shabaz's original idea
- Code: not started
- Current stage: architecture/design
- Hardware: not finalized

Current baseline architecture:

Emergency → Citizen/Victim → SOS / Incident Report → GPS / Camera / Audio inputs → AEGIS Platform → AI Intelligence → Incident Type / Severity / Risk Factors → AI Recommendation → Human Dispatcher Verification → Resource Selection → Live Tracking → Responder → Incident Resolution → Digital Case / Evidence / Timeline / Analytics → Post-Incident Analysis

Core philosophy:

- AI: Sense → Analyze → Recommend
- Human: Review → Decide → Dispatch
- AEGIS: Record → Track → Learn

AI does not independently control emergency response. Human dispatcher verification is part of the baseline architecture.

Design concepts such as ambulance, police, admin, and possible toll-plaza workflows must be marked as planned/design concepts.

If any future research suggests changing the architecture, create an explicit `ARCHITECTURE CHANGE PROPOSED` section containing:

- current architecture
- proposed change
- reason
- technical impact
- affected documents
- implementation impact
- approval status

Do not treat proposed architecture as the new baseline until Shabaz approves it.

## Project Boundaries

### AEGIS

Team project, architecture/design stage only. Do not describe as completed or implemented.

### MITRA

Internship project. Shabaz's confirmed scope is app-side Android development, integration, testing, RTSP handling, phone-camera fallback, navigation, TTS, voice interaction/wake-word app functionality, app controls/OCR/background behavior where applicable. Backend/model development belonged to another team.

### Skin Disease Classification

IEEE Pune internship project. Team of 3. Completed demo-level prototype. Exact model is unknown. Do not represent as a productized healthcare solution.

### NexCast Pro

Internship project done alone by Shabaz. Known stack: Python, Flask, OpenCV, Tesseract OCR, pdf2image / Poppler, pygame, HTML/CSS/vanilla JavaScript, REST APIs, JSON configuration. Known capabilities are limited to supplied documentation.

### VisionPay

Personal individual project. Confirmed: personally collected approximately 400 images per denomination for ₹10, ₹20, ₹50, ₹100, ₹200, and ₹500; MobileNetV2; TensorFlow Lite; real-time webcam inference; offline CPU-oriented inference; TTS; confidence/margin gating; temporal/majority smoothing; background class; auto-count mode; reported validation accuracy around 93% according to supplied project description.

Training code was AI-assisted. Do not claim every line of training code was manually written by Shabaz. Future ideas must not be presented as completed.

### Automotive BCM

Personal individual embedded project using ESP32. Demonstrates firmware/state-machine/event-loop work.

### Smart Wellness Desk Assistant

College team project using STM32 Nucleo-L476RG. Distinguish team output from Shabaz's confirmed hands-on contribution.

## Exclusions

NIDAR:

- Status: `EXCLUDED`
- Do not include in resumes or primary professional profile.
- May appear only in explicitly marked excluded files.
- Do not associate NIDAR with resume recommendations.

Hackathon project:

- Status: `EXCLUDED`
- Skipped because detailed files/details are unavailable.
- Do not invent details.

## Healthcare Research Initiative

Status: active research initiative.

Shabaz wants to conduct deep research into real healthcare problems and develop a product-level solution. Do not invent the healthcare problem, product, model, or architecture. These will be decided after research.

Structured state: `activity_state: ACTIVE_RESEARCH_INITIATIVE`. Unknowns remain `UNKNOWN` until Shabaz confirms them.

The old Skin Disease Classification internship project was demo-level. Do not falsely represent it as productized.

## Resume System

Two primary resume modes are supported.

Professional resume:

- Shabaz provides the prompt.
- The prompt determines length, formatting, target role, tone, ATS needs, project selection, and ordering.

Company-specific resume:

- Shabaz provides the company and states that it is visiting BITM and that he is applying.
- Use company requirements plus verified profile facts, relevant projects, verified skills, and verified experience.

Resume safety:

- Never invent.
- Never exaggerate.
- Never convert "worked with" into "led" unless confirmed.
- Never convert "project-level exposure" into "professional expertise".
- Never convert "planned" into "completed".
- Never convert "team project" into "individual project".
- Never include excluded projects unless explicitly authorized.

## Update Discipline

When new information is provided:

1. Identify the canonical owner file.
2. Preserve existing verified facts unless Shabaz explicitly corrects them.
3. Mark uncertain facts as `TO_VERIFY`.
4. Keep `PLANNED` facts out of completed sections.
5. Keep `EXCLUDED` facts out of primary profile and resume material.
6. Update project README and `facts.yaml` together when project facts change.
7. Record meaningful structural or factual changes in [`docs/CHANGELOG.md`](docs/CHANGELOG.md).
8. Run validation before commit.
