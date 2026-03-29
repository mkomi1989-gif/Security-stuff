# Login Attempt Monitoring System (Python)

## Overview
This is a simple Python system that simulates how login attempts are tracked in cybersecurity systems.

It monitors failed login attempts per user and triggers warnings or account locks based on thresholds.

---

## Features
- Tracks failed login attempts per user
- Warning triggered at 3 failed attempts
- Account lock triggered at 5 failed attempts
- Resets attempts after successful login
- Displays dynamic messages with attempt counts

---

## Concepts Used
- Python functions
- Dictionaries (per-user state tracking)
- Conditional logic (if / elif / else)
- f-strings for dynamic output

---

## Example Behavior
- User fails login → attempts increase
- At 3 attempts → warning message
- At 5 attempts → account locked
- Successful login → attempts reset to 0

---

## Purpose
This project is part of my cybersecurity learning path.

It simulates real SOC (Security Operations Center) logic such as:
- monitoring login behavior
- detecting suspicious activity
- triggering alerts

---

## Author
mkomi1989