## Features
- Real‑time monitoring of Windows Security Event Logs
- Incremental event processing (no duplicate reads)
- Detection of common security‑relevant events, including:
- Failed logon attempts
- Logon successes
- Event log clearing
- Persistent state tracking using a JSON file
- Console and file‑based alert output
- Lightweight Python implementation using pywin32

## How It Works
The Windows Log Tracker uses the win32evtlog API to read from the Security event channel.
It maintains a state.json file to remember the last processed record number, ensuring that each new run only processes new events. 

The tool performs three core tasks:
- Poll the Windows Security Log
- Parse and classify events
- Generate alerts when suspicious patterns are detected

## Getting Started
Prerequisites
- Windows 10/11
- Python 3.10+
- pywin32 package
pip install pywin32

Clone the Repository
git clone https://github.com/yourusername/WinLogTracker.git
cd WinLogTracker

Run the Program
python main.py

## Project Structure
WinLogTracker/
│
├── main.py               # Core log monitoring engine
├── state.json            # Tracks last processed event record
├── README.md             # Project documentation

## Example Output
[*] Windows Log Tracker started...
[ALERT] Failed login attempt from user: Administrator
[INFO] Processed 5 new events
[ALERT] Security log was cleared!

## Security Notes
This project is intended for educational and research purposes.
It does not replace enterprise‑grade SIEM tools, but it provides a clear, hands‑on demonstration of:
- Windows event log architecture
- System call behavior
- Basic intrusion detection logic
- Real‑time monitoring patterns

## Contributing
Contributions are welcome!
If you’d like to add new detection rules, improve parsing, or extend the tool to other event channels, feel free to open a pull request.

