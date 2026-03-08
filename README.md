## WinLogTracker

A lightweight Python tool for monitoring Windows Security Event Logs and detecting basic security-related activity such as failed login attempts and log clearing.

This project demonstrates how security monitoring systems analyze Windows logs and generate alerts.

## Features

Continuous monitoring of Windows Security Event Logs

Incremental event processing (prevents duplicate reads)

Detection of common security-relevant events, including:

4625 — Failed logon attempts

4624 — Successful logons

1102 — Security log cleared

Persistent state tracking using state.json

Console-based alert notifications

Lightweight Python implementation using pywin32

Simple architecture suitable for learning Windows log analysis

## How It Works

WinLogTracker uses the Windows Event Log API through the pywin32 library to read events from the Security event channel.

The system maintains a state.json file that stores the last processed record number, ensuring that each run only processes new log entries.

The monitoring engine performs three primary tasks:

Poll the Windows Security Log

Parse and classify events

Generate alerts when suspicious activity is detected

This design mimics how basic intrusion detection systems and SIEM log collectors operate.

## Getting Started
Prerequisites

Windows 10 / Windows 11

Python 3.10+

pywin32 package

Install the dependency:

pip install pywin32

## Clone the Repository
git clone https://github.com/Kndukauba/WinLogTracker
cd WinLogTracker

## Run the Program
python main.py

## Project Structure
WinLogTracker/
│
├── main.py        # Core log monitoring engine
├── state.json     # Tracks last processed event record
└── README.md      # Project documentation

## Example Output
[*] Windows Log Tracker started...

[ALERT] Failed login attempt from user: Administrator
[INFO] Processed 5 new events

[ALERT] Security log was cleared!

## Security Notes

This project is intended for educational and research purposes.

It does not replace enterprise-grade SIEM tools, but it provides a hands-on demonstration of:

Windows event log architecture

System call behavior

## Contributing

Contributions are welcome.

If you'd like to:

Add new detection rules

Improve event parsing

Extend the tool to other event channels

Feel free to open a pull request.

Basic intrusion detection logic

Real-time log monitoring patterns
