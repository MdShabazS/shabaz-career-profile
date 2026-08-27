# Tier-1 Skills Roadmap

A **development plan**, not a list of current claims. Nothing here may be copied into a resume, portfolio, or LinkedIn as a held skill. Current, verified levels are in [`current-skills.md`](current-skills.md); the market evidence behind this plan is in [`../research/TIER1_ROLE_RESEARCH.md`](../research/TIER1_ROLE_RESEARCH.md).

Two targets:

- **A. Tier-1 Software Developer**
- **B. Tier-1 Embedded Engineer**

## Priority scale

| Rank | Meaning |
|---|---|
| P0 | Critical — a gate. Without it, Tier-1 interviews stop early. |
| P1 | High — expected of a strong candidate. |
| P2 | Useful — differentiator / role-dependent. |
| P3 | Optional — nice to have, or awareness-level. |

"Current" reflects [`current-skills.md`](current-skills.md). "Target" is the level to reach for Tier-1 readiness.

---

## Track A — Tier-1 Software Developer

| Skill | Priority | Current | Target | Why it matters |
|---|---|---|---|---|
| DSA (arrays, strings, hashing, trees, graphs, DP, recursion) | P0 | Basic | Strong / interview-ready | The primary filter at Tier-1 companies; ≥2 coding rounds with LeetCode medium/hard patterns. |
| Problem-solving / pattern recognition (timed) | P0 | Basic | Strong | Online assessments are timed; recognizing the pattern fast matters more than volume. |
| One strong language (recommend C++ or Java for DSA) | P0 | Basic | Proficient | Interviews are language-agnostic but demand fluency in one. C++/Java are standard for DSA. |
| Git / version control | P0 | Basic | Proficient | Baseline for any team; expected in every posting. |
| OOP | P1 | Not claimed | Working | Design questions and code-quality expectations assume OOP fluency. |
| DBMS + SQL (joins, indexing, normalization, transactions) | P1 | Basic | Working | Named explicitly in most SWE job families; SQL round is common. |
| Operating Systems (processes/threads, scheduling, memory, deadlocks) | P1 | Basic | Working | Core CS-fundamentals interview area. |
| Computer Networks (TCP/IP, HTTP, DNS basics) | P1 | Basic | Working | Fundamentals round; underpins API/system-design answers. |
| Testing & debugging | P1 | Basic (project) | Working | SDLC participation is a listed responsibility; unit testing expected. |
| APIs (REST, request/response, JSON) | P1 | Project exposure | Working | Application/backend roles assume it; you have NexCast Pro exposure to build on. |
| Concurrency & memory management | P2 | Not claimed | Aware → working | Shows depth; more prominent for systems/backend roles. |
| System design fundamentals | P2 | Not claimed | Aware | Minimal for most new-grad roles, but a differentiator; learn the vocabulary. |
| Software engineering practices (code review, SDLC, clean code) | P2 | Basic | Working | Signals professionalism; reinforced by internship work. |
| Build systems / CI/CD | P3 | Basic (Gradle exposure) | Aware | Role-dependent; awareness is enough for entry level. |
| Linux / command line | P2 | Not claimed | Working | Expected working comfort; used across dev and embedded. |

### Prerequisites, learning order, and application (Software)

1. **Language + Git first** (P0): pick C++ or Java, get fluent, use Git daily. *Prereq for everything below.*
2. **DSA + timed problem-solving** (P0): work patterns (e.g. a structured 150-problem set). *Interview relevance: highest.* Application: track progress publicly on GitHub.
3. **OOP** (P1) alongside the chosen language.
4. **DBMS/SQL, OS, CN** (P1): the CS-fundamentals trio. *Interview relevance: dedicated rounds.* Application: add a small SQL-backed feature/project.
5. **Testing, APIs, Linux** (P1/P2): apply on a real project — extend NexCast Pro or a new API service with unit tests.
6. **System design basics + concurrency** (P2): after DSA is solid.
7. **CI/CD awareness** (P3): wire a GitHub Actions pipeline on one project.

**Project ideas:** a REST API service with a database and tests; a small full-stack app; publish DSA solutions with clean READMEs.

---

## Track B — Tier-1 Embedded Engineer

| Skill | Priority | Current | Target | Why it matters |
|---|---|---|---|---|
| C (embedded, pointers, memory, bit manipulation) | P0 | Basic | Strong | The #1 hiring filter for embedded in 2026. |
| MCU architecture + ARM Cortex-M fundamentals | P0 | Exposure (ESP32/STM32) | Working | Core to the role; Cortex-M is the common target. |
| GPIO, timers, interrupts, PWM, ADC | P0 | Project exposure | Working | Bread-and-butter peripheral work; expected hands-on. |
| Communication protocols: UART, SPI, I2C | P0 | Incidental (I2C on STM32) | Working | Named in nearly every embedded posting. |
| Debugging (logic, hardware, serial) + JTAG/SWD | P1 | Basic (serial) | Working | Low-level debugging with JTAG/SWD is a stated requirement. |
| RTOS / FreeRTOS (tasks, scheduling, sync) | P1 | Not claimed | Working | Mandatory in automotive/robotics/industrial embedded. |
| Embedded C++ | P2 | Basic | Working | Increasingly used; strengthens firmware roles. |
| DMA | P2 | Not claimed | Aware → working | Efficiency/throughput topic; interview depth signal. |
| Bootloaders & firmware architecture | P2 | Not claimed | Aware | Shows systems maturity. |
| Embedded Linux + device drivers | P2 | Not claimed | Aware | Role-dependent (Linux-class devices); high value where required. |
| Testing (unit, HIL) | P1 | Basic | Working | Verification is the most effort-intensive part of safety-critical work. |
| Version control / build for embedded | P1 | Basic | Working | Same Git baseline; plus embedded toolchains. |

### Automotive specialization (P2–P3, awareness for now)

Relevant because Automotive is a stated interest and Automotive BCM is a portfolio project. For entry level these are **awareness**, deepened later.

| Topic | Priority | Target | Note |
|---|---|---|---|
| CAN / LIN bus | P2 | Working (if automotive) | Automotive networking basics. |
| Diagnostics (UDS/OBD awareness) | P3 | Aware | Deepen only for automotive roles. |
| MISRA C concepts | P2 | Aware | Coding-standard discipline for safety code. |
| Functional safety (ISO 26262 / ASIL) concepts | P3 | Aware | Understand the vocabulary and intent. |
| AUTOSAR awareness | P3 | Aware | Architecture concept; not hands-on at entry. |
| ASPICE awareness | P3 | Aware | Process-quality framework; awareness only. |

### Prerequisites, learning order, and application (Embedded)

1. **Strong C** (P0): pointers, memory, bit-ops. *Prereq for all firmware.* Application: refactor Automotive BCM with cleaner abstractions.
2. **MCU + Cortex-M fundamentals** (P0): registers, clock, memory map on STM32.
3. **Peripherals: GPIO, timers, interrupts, PWM, ADC** (P0): build interrupt-driven, non-blocking firmware.
4. **UART, SPI, I2C** (P0): interface real sensors/displays over each bus. *Interview relevance: very high.*
5. **Debugging + JTAG/SWD** (P1): move from `printf` to a hardware debugger.
6. **RTOS / FreeRTOS** (P1): port a project to tasks with proper synchronization. *Interview relevance: high, gate for automotive/robotics.*
7. **Testing, DMA, bootloaders** (P1/P2).
8. **Automotive stack (CAN/LIN, MISRA, ISO 26262 awareness)** (P2/P3): if pursuing automotive.
9. **Embedded Linux / drivers** (P2): if targeting Linux-class roles.

**Project ideas:** an interrupt-driven multi-sensor system over I2C/SPI/UART; the same project ported to FreeRTOS; a CAN-bus demo between two boards; extend Automotive BCM toward a small automotive networking demo.

---

## Gap summary (biggest levers first)

- **Both tracks share a P0 base:** strong C/C++ or Java, DSA + problem-solving, and Git. These move the needle most.
- **Software P0/P1 gaps:** DSA depth, OOP, and turning Basic DBMS/OS/CN into working interview knowledge.
- **Embedded P0/P1 gaps:** turning peripheral exposure (GPIO/timers/ADC/I2C) into confident, interrupt-driven work across UART/SPI/I2C, plus RTOS/FreeRTOS and hardware debugging (JTAG/SWD).
- **Automotive** is a differentiator layer (awareness now, depth later).

Review this file whenever a real job description is available, and map its requirements against the current level before deciding what to study next.
