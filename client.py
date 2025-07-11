from pynput import keyboard
import requests

KEY = 'w'
BASE_URL = ""

def notify_server():
    requests.post(BASE_URL + "/ping")

def process_key_press(key):
    if key.char == KEY:
        notify_server()

def main():
    with keyboard.Listener(on_press=process_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()