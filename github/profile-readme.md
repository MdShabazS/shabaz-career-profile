<!-- Profile banner -->
<p align="center">
  <img src="./assets/profile-banner.png" alt="Mohammed Shabaz S — Embedded Engineer and Automotive Embedded Systems: firmware, microcontrollers, real-time systems on ESP32 and STM32" width="100%"/>
</p>

<p align="center">
  <img alt="B.E. ECE, BITM" src="https://img.shields.io/badge/B.E._ECE-BITM-0b1220?style=for-the-badge&labelColor=0b1220&color=38BDF8"/>
  <img alt="CGPA 8.38" src="https://img.shields.io/badge/CGPA-8.38-0b1220?style=for-the-badge&labelColor=0b1220&color=34D399"/>
  <img alt="Expected graduation 2027" src="https://img.shields.io/badge/Expected-2027-0b1220?style=for-the-badge&labelColor=0b1220&color=F59E0B"/>
  <img alt="Focus: Embedded and Automotive" src="https://img.shields.io/badge/Focus-Embedded_%7C_Automotive-0b1220?style=for-the-badge&labelColor=0b1220&color=2563EB"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/shabaz17/"><img alt="LinkedIn: shabaz17" src="https://img.shields.io/badge/LinkedIn-shabaz17-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/MdShabazS"><img alt="GitHub: MdShabazS" src="https://img.shields.io/badge/GitHub-MdShabazS-181717?style=flat-square&logo=github&logoColor=white"/></a>
  <a href="mailto:md.shabaz.2005@gmail.com"><img alt="Email: md.shabaz.2005 at gmail" src="https://img.shields.io/badge/Email-md.shabaz.2005-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>
</p>

---

## Professional Snapshot

| Area | Details |
|---|---|
| **Current** | Final-year B.E. Electronics & Communication Engineering, BITM · Student Intern @ Nokia |
| **Primary track** | Embedded Engineer · Automotive Embedded Systems |
| **Secondary** | Software Engineering |
| **Supporting** | AI / Computer Vision |
| **Engineering focus** | Microcontroller firmware, finite-state machines, non-blocking real-time control |
| **Education** | BITM · Expected 2027 · CGPA 8.38 |

I build embedded and automotive firmware — microcontroller systems, state machines and deterministic real-time loops in Embedded C/C++ on ESP32 and STM32 (ARM Cortex-M) — and back it with practical software and computer-vision work. Currently working as a Student Intern at Nokia.

---

## Focus

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>🚗 Automotive &amp; Embedded</h3>
      <p>Firmware for microcontrollers — finite-state machines, sensor interfacing, GPIO/I2C/ADC, and non-blocking real-time control, including automotive-oriented prototypes on ESP32 and STM32 (ARM Cortex-M4).</p>
    </td>
    <td width="33%" valign="top">
      <h3>💻 Software</h3>
      <p>Practical software in C, C++, Python and SQL, with Android Studio and Git/GitHub. I care about clean, testable, debuggable code and predictable behaviour.</p>
    </td>
    <td width="33%" valign="top">
      <h3>👁️ AI / Computer Vision</h3>
      <p>Project-level work with OpenCV, TensorFlow Lite and MobileNetV2 — real-time, offline inference pipelines that run on plain CPUs.</p>
    </td>
  </tr>
</table>

---

## Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=c,cpp,python,arduino,opencv,tensorflow,androidstudio,git,github&perline=9" alt="Core technologies: C, C++, Python, Arduino, OpenCV, TensorFlow, Android Studio, Git, GitHub"/>
</p>

- **Embedded &amp; Firmware:** Embedded C · Microcontrollers · ARM Cortex-M4 · finite-state machines · non-blocking real-time design · GPIO · I2C · ADC · timers · sensor interfacing · debugging
- **Platforms &amp; Tools:** ESP32 · STM32 (Nucleo-L476RG) · STM32CubeIDE · Arduino · Android Studio · Git/GitHub
- **Programming:** C · C++ · Embedded C · Python · SQL
- **AI / Computer Vision:** OpenCV · TensorFlow Lite · MobileNetV2 · Text-to-Speech
- **CS Foundations:** Data Structures &amp; Algorithms · Operating Systems · DBMS · Computer Networks

<sub>Learning next (not current skills): UART/SPI · RTOS/FreeRTOS · CAN-bus networking toward automotive systems.</sub>

---

## Featured Projects

<h3><a href="https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32">Automotive Body Control Module</a> &nbsp;<sub>Individual · Embedded / Automotive</sub></h3>

<a href="https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32"><img src="./assets/project-bcm.png" alt="Automotive Body Control Module — ESP32 breadboard build with OLED dashboard, rotary ignition switch, buzzer and wiring" width="560"/></a>

ESP32 firmware modelling a vehicle body-control ECU (photo: the actual breadboard build).

- **OFF/ACC/ON ignition FSM** driving 6+ functions — indicators, synchronized hazard, brake logic, buzzer, OLED dashboard.
- Non-blocking `millis()` loop (zero `delay()`), 30&nbsp;ms brake debounce, 10&nbsp;Hz I2C OLED refresh, clean GPIO abstraction, edge-triggered logging.
- **Stack:** ESP32 · Arduino/C++ · Finite-State Machine · GPIO · I2C OLED &nbsp;—&nbsp; [Repository →](https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32)

<h3><a href="https://github.com/MdShabazS/Smart-Wellness-Desk-Assistant">Smart Wellness Desk Assistant</a> &nbsp;<sub>College team project · Embedded</sub></h3>

<a href="https://github.com/MdShabazS/Smart-Wellness-Desk-Assistant"><img src="./assets/project-smart-wellness.png" alt="Smart Wellness Desk Assistant — STM32 Nucleo-L476RG wiring diagram showing ultrasonic sensor, temperature sensor, I2C OLED and buzzer" width="560"/></a>

STM32 desk-wellness device on ARM Cortex-M4 (image: the project wiring diagram).

- Ultrasonic presence + 12-bit ADC temperature sensing, I2C SSD1306 OLED and timer-driven alerts via a non-blocking finite-state machine.
- **My contribution:** sensor interfacing, wiring, and testing/debugging in STM32CubeIDE within the team.
- **Stack:** STM32 Nucleo-L476RG · ARM Cortex-M4 · STM32 HAL · STM32CubeIDE · Embedded C &nbsp;—&nbsp; [Repository →](https://github.com/MdShabazS/Smart-Wellness-Desk-Assistant)

<h3><a href="https://github.com/MdShabazS/visionpay">VisionPay</a> &nbsp;<sub>Individual · AI / Computer Vision</sub></h3>

<a href="https://github.com/MdShabazS/visionpay"><img src="./assets/project-visionpay.png" alt="VisionPay — real-time Indian currency detection reading a 500 rupee note at 93% confidence with spoken output" width="560"/></a>

Offline, real-time Indian-currency detector with spoken output for visually impaired users.

- ~400 images/denomination across 6 classes (₹10–₹500); MobileNetV2 → TensorFlow Lite (~93% reported validation accuracy), running offline on CPU.
- Confidence/margin gating, temporal smoothing, a background class and an auto-count mode.
- **Stack:** Python · OpenCV · TensorFlow Lite · MobileNetV2 · Text-to-Speech &nbsp;—&nbsp; [Repository →](https://github.com/MdShabazS/visionpay)

---

## 🚧 Currently Building

- **[AEGIS](https://github.com/MdShabazS/aegis)** — an AI-assisted emergency-response platform where **AI recommends and a human dispatcher decides**. *Team project · architecture / design stage — not yet built.*
- **Automotive-embedded depth** — moving from I2C toward UART/SPI, an RTOS/FreeRTOS port, and a CAN-bus build. *(Learning goals — not presented as current skills.)*

---

## Experience &amp; Leadership

<table>
  <tr>
    <td width="55%" valign="top">
      <h3>Experience</h3>
      <ul>
        <li><b>Nokia Solutions and Networks India</b> — Student Intern. Currently working as a Student Intern at Nokia.</li>
        <li><b>iHelp Robotics</b> — AI Research Intern – Deep Learning &amp; Model Development (Mar–Aug 2026). On <b>MITRA</b>, an assistive-vision Android app, I worked the app side: camera-stream reliability, offline voice-command robustness, and multi-device testing. Backend and model belonged to a separate team.</li>
        <li><b>IEEE EMBS Pune Section</b> — Skin Disease Classification (1 month, 3-member team). Model selection, training and evaluation plus Python image-processing — a demo-level prototype.</li>
      </ul>
    </td>
    <td width="45%" valign="top">
      <h3>Leadership</h3>
      <ul>
        <li>Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM <sub>(previously Treasurer)</sub></li>
        <li>Treasurer, BITM Robotics Club</li>
        <li>Google Student Ambassador (2025)</li>
        <li>Selected Participant, IEEE SPACE 2026 — B.Tech Initiative</li>
      </ul>
    </td>
  </tr>
</table>

---

## GitHub Activity

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=MdShabazS&theme=tokyonight" alt="GitHub profile summary for MdShabazS"/>
</p>

---

## Let's Connect

<p align="center">
  <a href="https://www.linkedin.com/in/shabaz17/"><img alt="Connect on LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:md.shabaz.2005@gmail.com"><img alt="Reach out by email" src="https://img.shields.io/badge/Email-Reach_out-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://github.com/MdShabazS"><img alt="Follow on GitHub" src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:07111F,50:0E2332,100:12303F&height=90&section=footer" alt=""/>
</p>
