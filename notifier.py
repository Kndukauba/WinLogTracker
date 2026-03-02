def notify(alert): 
  message = f"[ALERT] {alert}"
  print(message)

  with open("alerts.log", "a") as file: 
    file.write(message + "\n")