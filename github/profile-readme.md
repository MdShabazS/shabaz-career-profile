<h1 align="center">Mohammed Shabaz S</h1>

<p align="center"><strong>Embedded Engineer&nbsp;|&nbsp;Automotive Embedded Systems</strong></p>

<p align="center">Firmware · Microcontrollers · Real-Time Systems&nbsp;&nbsp;·&nbsp;&nbsp;Ballari, Karnataka, India</p>

---

### About

I build embedded and automotive firmware — microcontroller systems, finite-state machines, and non-blocking real-time control in **Embedded C/C++ on ESP32 and STM32 (ARM Cortex-M)**. I'm a final-year Electronics & Communication Engineering student at BITM (CGPA 8.38, graduating 2027), currently a Student Intern at Nokia. When a problem needs it, I also build small offline computer-vision tools in Python. I care about systems that behave predictably: clean state machines, deterministic loops, and firmware I can debug and trust.

- **Focus:** Embedded / automotive firmware, real-time systems, core electronics
- **Also:** Software engineering · applied computer vision (OpenCV, TensorFlow Lite)
- **Learning next:** UART/SPI, RTOS/FreeRTOS, and CAN-bus networking toward automotive systems
- **Location:** Ballari, Karnataka, India

### Experience

- **Nokia Solutions and Networks India** — Student Intern *(16 September 2026 – Present)*. Currently working as a Student Intern at Nokia.
- **iHelp Robotics** — AI Research Intern – Deep Learning & Model Development *(23 March – 23 August 2026)*. On **MITRA**, an assistive-vision Android app, I worked the app side: camera-stream reliability, offline voice-command robustness, and multi-device testing. Backend and model belonged to a separate team.
- **IEEE EMBS Pune Section** — Skin Disease Classification internship *(1 month, 3-member team)*. Model selection, training and evaluation plus Python image-processing — a demo-level prototype.

### Featured Projects

**[Automotive Body Control Module](https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32)** — ESP32 firmware that simulates a vehicle body-control ECU.
`Stack: ESP32 · Arduino/C++ · Finite-State Machine · GPIO · I2C OLED`
- OFF/ACC/ON ignition state machine driving 6+ functions: turn indicators, synchronized hazard, brake logic, buzzer and an OLED dashboard.
- Non-blocking `millis()` scheduler (zero `delay()` in the loop) with 30 ms brake debouncing, throttled 10 Hz I2C OLED refresh, a clean GPIO abstraction and edge-triggered serial logging.

**[Smart Wellness Desk Assistant](https://github.com/MdShabazS/Smart-Wellness-Desk-Assistant)** — STM32 desk-wellness device *(college team project)*.
`Stack: STM32 Nucleo-L476RG (ARM Cortex-M4) · STM32 HAL · STM32CubeIDE · Embedded C`
- Ultrasonic presence and 12-bit ADC temperature sensing, an I2C SSD1306 OLED and timer-driven buzzer alerts, coordinated by a non-blocking finite-state machine.
- My part: sensor interfacing, wiring, and testing/debugging in STM32CubeIDE within the team.

**[VisionPay](https://github.com/MdShabazS/visionpay)** — offline, real-time Indian-currency detector with spoken output, for visually impaired users.
`Stack: Python · OpenCV · TensorFlow Lite · MobileNetV2 · Text-to-Speech`
- ~400 images per denomination across 6 classes (₹10–₹500); MobileNetV2 exported to TensorFlow Lite (~93% reported validation accuracy), running offline on CPU.
- Reliability from confidence/margin gating, temporal smoothing, a background class and an auto-count mode.

### Currently Working On

- **AEGIS** — an AI-assisted emergency-response platform (AI recommends, a human dispatcher decides). *Team project, design/early stage — architecture first, not yet built.*
- **Automotive embedded depth** — moving from I2C toward UART/SPI, an RTOS/FreeRTOS port, and a CAN-bus build to grow into automotive networking. *(Learning goals, not current skills.)*

### Technical Skills

- **Embedded & Firmware:** Embedded C · Microcontrollers · ARM Cortex-M4 · finite-state machines · non-blocking real-time design · GPIO · I2C · ADC · timers · sensor interfacing · debugging
- **Platforms & Tools:** ESP32 · STM32 (Nucleo-L476RG) · STM32CubeIDE · Arduino · Android Studio · Git/GitHub
- **Programming:** C · C++ · Embedded C · Python · SQL
- **AI / Computer Vision:** OpenCV · TensorFlow Lite · MobileNetV2 · Text-to-Speech
- **CS Foundations:** Data Structures & Algorithms · Operating Systems · DBMS · Computer Networks

### Education & Leadership

- **B.E. Electronics & Communication Engineering**, Ballari Institute of Technology and Management (BITM) — Final Year, expected 2027 · CGPA 8.38
- Vice-Chair, IEEE CAS Society (IEEE Student Branch BITM) · Treasurer, BITM Robotics Club · Google Student Ambassador (2025)

### Contact

- **Email:** [md.shabaz.2005@gmail.com](mailto:md.shabaz.2005@gmail.com)
- **LinkedIn:** [linkedin.com/in/shabaz17](https://www.linkedin.com/in/shabaz17/)
- **GitHub:** [github.com/MdShabazS](https://github.com/MdShabazS)
