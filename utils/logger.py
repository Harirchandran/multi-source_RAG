# utils/logger.py

import datetime


def log(message, data=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] {message}")

    if data:
        print(data)