from datetime import datetime

def log(message):
    timestamp = datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")
