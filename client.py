from pynput import keyboard
import requests
from dotenv import load_dotenv
import os

load_dotenv()

KEY = 'w'
BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")

def notify_server():
    try:
        r = requests.post(
            f"{BASE_URL}/ping",
            headers={"X-Token": TOKEN},
            data=""                   
        )
        print("[client]  ", r.status_code, r.text)
    except Exception as exc:
        print("[client]  Request failed:", exc)


def process_key_press(key):
    try:
        if key.char and key.char.lower() == KEY:
            notify_server()
    except AttributeError:
        # Key.space, Key.shift, etc. -> just ignore
        pass
        

def main():
    with keyboard.Listener(on_press=process_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()