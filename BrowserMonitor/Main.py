import sqlite3
import time
import subprocess
from logging import exception
from pathlib import Path
from osscripts import delete_tabs,delete_history
from Ai import reasoning


def get_table():
    path = r"/Users/air/Library/Safari/History.db"
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    history = cursor.execute("SELECT * FROM history_items")
    return history


while True:
    try:
        time.sleep(10)
        items = get_table()
        sorted_history = [item[1] for item in items if item[1] is not None][-6:]
        message = reasoning(sorted_history)
        if message == "no":
            subprocess.run(["osascript", "-e", delete_history()])
            subprocess.run(["osascript", "-e", delete_tabs()])
            subprocess.run(["pkill", "-x", "Safari"])
            time.sleep(2)
    except Exception as e:
        pass