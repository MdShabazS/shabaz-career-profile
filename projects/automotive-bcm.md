# Automotive BCM (Body Control Module)

| Field | Value | Status |
|---|---|---|
| Type | Individual embedded project | `VERIFIED` |
| Platform | ESP32 | `VERIFIED` |
| Lifecycle | `COMPLETED` | — |
| GitHub | https://github.com/MdShabazS/Automotive-Body-Control-Module-ESP32 | `VERIFIED` |

## Overview

An ESP32-based Automotive Body Control Module prototype that simulates ignition and vehicle body-control behaviour. The focus is firmware structure, a state machine, and non-blocking event-loop design.

## Features

- OFF / ACC / ON ignition finite-state machine
- Brake control with debouncing
- Left/right indicators and a synchronized hazard mode
- Non-blocking `millis()`-based scheduling
- Buzzer feedback
- OLED dashboard
- Edge-triggered serial logging
- GPIO abstraction

## Positioning

Embedded / automotive firmware project demonstrating state-machine and real-time event-loop design. Individual work — do not attribute to a team.
