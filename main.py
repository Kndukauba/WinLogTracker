import win32evtlog
import time
import json
from detectors import analyze_events
from notifier import notify

# Load config
with open("config.json") as file:
    config = json.load(file)

# Load state
try:
    with open("state.json") as f:
        state = json.load(f)
except FileNotFoundError:
    state = {"last_record_number": 0}

LOG_NAME = config["log_name"]
POLL_INTERVAL = config["poll_interval_seconds"]

server = 'localhost'
log_handle = win32evtlog.OpenEventLog(server, LOG_NAME)

print("[*] Windows Log Auditor started..")

while True:
    # Get log boundaries
    total_records = win32evtlog.GetNumberOfEventLogRecords(log_handle)
    oldest_record = win32evtlog.GetOldestEventLogRecord(log_handle)
    newest_record = oldest_record + total_records - 1

    # Last processed record
    last_record = state.get("last_record_number", oldest_record)

    # Clamp to valid range
    if last_record < oldest_record:
        last_record = oldest_record
    if last_record > newest_record:
        last_record = newest_record

    # Offset must be a valid record index
    offset = last_record

    flags = win32evtlog.EVENTLOG_SEEK_READ | win32evtlog.EVENTLOG_FORWARDS_READ

    try:
        events = win32evtlog.ReadEventLog(log_handle, flags, offset)
    except Exception as e:
        print(f"[ERROR] Failed reading log: {e}")
        time.sleep(POLL_INTERVAL)
        continue

    if events:
        # Filter out events we've already processed
        new_events = [ev for ev in events if ev.RecordNumber > last_record]

        print(f"[DEBUG] Read {len(new_events)} new events")

        if new_events:
            alerts = analyze_events(new_events, config)
            for alert in alerts:
                notify(alert)

            # Update last_record_number ONLY if newer events exist
            newest_seen = new_events[-1].RecordNumber
            state["last_record_number"] = newest_seen

            with open("state.json", "w") as f:
                json.dump(state, f, indent=2)

    time.sleep(POLL_INTERVAL)