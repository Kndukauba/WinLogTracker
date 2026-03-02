from time import time

FAILED_LOGIN_WINDOW = 60
failed_login_times = []

def analyze_events(events, config):
    alerts = []
    now = time()

    FAILED_LOGIN_THRESHOLD = config["alert_thresholds"]["failed_logins"]

    for event in events:
        event_id = event.EventID & 0xFFFF
        time_generated = event.TimeGenerated.Format()

        if event_id == config["event_ids"]["failed_login"]:
            failed_login_times.append(now)

            failed_login_times[:] = [
                t for t in failed_login_times
                if now - t <= FAILED_LOGIN_WINDOW
            ]

            if len(failed_login_times) >= FAILED_LOGIN_THRESHOLD:
                alerts.append({
                    "type": "FAILED_LOGIN_BRUTE_FORCE",
                    "count": len(failed_login_times),
                    "window_seconds": FAILED_LOGIN_WINDOW,
                    "time": time_generated
                })
                failed_login_times.clear()

        if event_id == config["event_ids"]["log_cleared"]:
            alerts.append({
                "type": "LOG_CLEARED",
                "time": time_generated
            })

    return alerts