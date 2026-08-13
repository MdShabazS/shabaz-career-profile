# Mohammed Shabaz S - Master ATS Resume

This file is the reusable base for professional resumes. Use it when preparing company-specific resumes, but tailor the project order, skills, and summary to the target role/JD.

## Resume Rules

- Use a clean one-column resume format for ATS.
- Keep the resume to one page for campus placements unless a company specifically allows more.
- Do not invent scores, metrics, titles, responsibilities, tools, links, or certificates.
- Do not present planned certifications as completed.
- Do not include sensitive identifiers, private project links, passport details, phone numbers stored in screenshots, or offer-letter-only details.
- Keep MITRA contribution limited to Android app-side work; backend and model development belonged to another team.
- Keep Skin Disease Classification as a demo-level internship project.
- Keep AEGIS as an architecture/design-stage team project unless implementation is later verified.
- Add company-specific keywords only when supported by verified experience.

## ATS Strategy

Target role families:

- Software Engineer / Software Developer
- Embedded Software Engineer / Embedded Engineer
- Application Development Intern / Trainee

Strong keyword groups to use when relevant:

- Programming: Python, C, C++, Embedded C, Java, SQL
- Software: Android Studio, REST APIs, Git, GitHub, Firebase Realtime Database
- AI/ML: OpenCV, TensorFlow Lite, MobileNetV2, image processing, model evaluation
- Embedded: ESP32, STM32, STM32CubeIDE, STM32 HAL, Arduino IDE, sensors, timers, OLED, state machine
- CS fundamentals: Data Structures, DBMS, Operating Systems
- Professional: testing, debugging, team coordination, technical event coordination

Avoid weak or unsupported claims:

- expert, advanced, production-grade, deployed, scalable cloud system, end-to-end AI platform
- backend/model ownership for MITRA
- completed implementation for AEGIS
- productized medical system for Skin Disease Classification

## Base Resume

```markdown
# Mohammed Shabaz S

B.E. Electronics and Communication Engineering | Ballari Institute of Technology and Management  
GitHub: https://github.com/MdShabazS | LinkedIn: [Add verified LinkedIn URL] | Email: [Add email] | Phone: [Add phone] | Location: [Add city, state]

## Summary

Electronics and Communication Engineering student with an 8.38 CGPA and hands-on experience across Android application development, embedded systems and AI/ML-based projects. Built and tested projects using Python, C/C++, Embedded C, OpenCV, TensorFlow Lite, ESP32, STM32 and REST APIs. Currently strengthening Java, DSA, SQL and core computer science fundamentals for software and embedded placement roles.

## Education

**Ballari Institute of Technology and Management, Bellary**  
B.E. in Electronics and Communication Engineering | Expected 2027  
CGPA: 8.38

**Class 12** - 80%  
**Class 10** - 86.88%

## Technical Skills

**Languages:** Python, C, C++, Embedded C, Java, SQL  
**Software & Tools:** Git, GitHub, Android Studio, REST APIs, Firebase Realtime Database  
**AI/ML & Computer Vision:** OpenCV, TensorFlow Lite, MobileNetV2, image processing  
**Embedded Systems:** ESP32, STM32 Nucleo-L476RG, STM32CubeIDE, STM32 HAL, Arduino IDE, sensors, timers, OLED  
**Core CS:** Data Structures, DBMS, Operating Systems

## Experience

**AI Research Intern - Deep Learning & Model Development**  
iHelp Robotics Private Limited | Remote | Mar 2026 - Present

- Developed and tested Android app-side features for MITRA, an assistive-vision system for blind and low-vision users.
- Improved app workflows involving RTSP stream handling, phone-camera fallback, navigation, TTS, voice interaction related features and OCR/app controls.
- Worked in a remote internship environment and gained practical exposure to real-time assistive vision workflows and AI/software integration.

**Student Intern - Skin Disease Classification**  
IEEE EMBS Pune Chapter / IEEE Pune Section | Remote | Jun 2026

- Completed a one-month online internship on Skin Disease Classification as part of a 3-member team.
- Worked on model selection, model training, model evaluation, Python coding, image processing, UI/application work and testing.
- Built a demo-level classification workflow and strengthened practical understanding of AI/ML project development and evaluation.

**Pega National Internship Program Trainee**  
Pega Systems in collaboration with SmartBridge | Remote | In Progress

- Participating in a 60-hour application-development program with live technical sessions, self-paced modules, labs and mentor-supported learning.
- Working through capstone-oriented learning tasks with epics and user stories tracked through a Kanban workflow.

## Projects

**VisionPay - Real-Time Indian Currency Detection**  
Python, OpenCV, TensorFlow Lite, MobileNetV2, TTS

- Built a personal project for Indian currency denomination detection with spoken feedback for visually impaired users.
- Collected approximately 400 images per denomination across 6 Indian currency classes: INR 10, INR 20, INR 50, INR 100, INR 200 and INR 500.
- Trained a MobileNetV2-based model, converted it to TensorFlow Lite and reported approximately 93% validation accuracy.
- Implemented webcam inference with confidence checks, majority smoothing, background class handling and auto-count mode.
- GitHub: https://github.com/MdShabazS/visionpay

**Automotive Body Control Module**  
ESP32, Embedded C, OLED, GPIO, State Machine

- Built an ESP32-based Automotive Body Control Module prototype for ignition and vehicle control simulation.
- Implemented OFF/ACC/ON ignition states, brake control, left/right indicators, synchronized hazard mode, buzzer feedback and OLED dashboard output.
- Structured firmware using non-blocking millis-based scheduling, brake debouncing, GPIO abstraction and edge-triggered serial logging.
- GitHub: https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32

**Smart Wellness Desk Assistant**  
STM32 Nucleo-L476RG, STM32 HAL, Embedded C, Sensors

- Built and tested embedded modules for a college team project using STM32 Nucleo-L476RG to support healthier desk habits through sensing and feedback.
- Handled sensor interfacing, hardware wiring, testing and debugging using STM32CubeIDE and STM32 HAL.
- Worked with ultrasonic sensing, ADC temperature sensing, I2C OLED feedback, timers and buzzer alerts.
- GitHub: https://github.com/MdShabazS/Smart-Wellness-Desk-Assistant

**AEGIS - AI-Assisted Emergency Response Platform**  
Architecture/Design Stage | Team Project

- Leading a 3-member team project based on an original idea for an AI-assisted emergency response platform.
- Designed the baseline workflow for incident reporting, GPS/camera/audio inputs, AI-based analysis, human dispatcher verification, resource selection, live tracking and post-incident records.
- Defined a responsibility model where AI recommends actions and a human dispatcher verifies decisions before response assignment.

## Leadership And Activities

- Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM; previously served as Treasurer.
- Treasurer, BITM Robotics Club.
- Selected as Google Student Ambassador in 2025.
- Active IEEE student member since 2023.
- Volunteered for Explorika 2K24 at Ballari Institute of Technology and Management.

## Certifications

- Google Cloud Generative AI Virtual Internship - SmartBridge and SmartInternz, 2025.
- Embedded Systems Training - Internshala Trainings, 2025.
- Python Programming Internship Certificate, 2024.
- IEEE EMBS National Student Internship Program - Skin Disease Classification, 2026.

## Languages

English, Hindi, Kannada, Urdu
```

## Software Role Version

Use this project order for software companies:

1. MITRA
2. VisionPay
3. Skin Disease Classification
4. AEGIS
5. Automotive Body Control Module

Recommended summary:

```text
ECE student with an 8.38 CGPA and hands-on experience in Android application development, Python-based AI/ML projects, REST APIs, OpenCV, TensorFlow Lite and Git/GitHub. Worked on internship and personal projects involving assistive technology, real-time camera workflows, currency recognition, image processing and application testing. Currently strengthening Java, DSA, SQL and core computer science fundamentals for software development roles.
```

## Embedded Role Version

Use this project order for embedded companies:

1. Automotive Body Control Module
2. Smart Wellness Desk Assistant
3. MITRA
4. VisionPay
5. AEGIS

Recommended summary:

```text
ECE student with an 8.38 CGPA and hands-on experience in embedded systems, C/C++, Embedded C, ESP32, STM32, STM32CubeIDE and hardware debugging. Built projects involving state-machine based automotive control, sensor interfacing, OLED feedback, timers and embedded event loops, with additional exposure to Android and AI/ML-based assistive technology projects.
```

## Company-Specific Tailoring Checklist

Before creating a company-specific resume:

1. Paste the JD or company role requirements.
2. Identify role type: software, embedded, AI/ML, testing, or mixed.
3. Pick 3-4 strongest matching projects.
4. Move matching skills to the front of the skills section.
5. Add only verified certifications relevant to the JD.
6. Remove weaker or unrelated sections to keep the resume one page.
7. Keep wording natural and specific; avoid generic AI-style sentences.
8. Run a final check for truthful ownership, dates and technologies.

## Details To Verify Before Final PDF

- Email address
- Phone number
- LinkedIn URL
- City/state
- Exact dates for IEEE CAS Vice-Chair and Ex-Treasurer roles
- Exact dates for BITM Robotics Club Treasurer role
- Whether to include NexCast Pro for a specific company resume
- Whether to include percentage details for Class 10 and Class 12
