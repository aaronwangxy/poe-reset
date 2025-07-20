from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import random
import threading
import pyperclip

kbd = KeyboardController()
mouse = MouseController()

TARGET_STRING = ""

DELAY_MS = 200
DELAY_DELTA_MS = 30
RELEASE_DELAY_MS = (30, 70)  # in ms

START_KEY = ','
END_KEY = '.'
EXIT_KEY = '/'

clicking = False
click_thread = None

def copy_clipboard():
    """Simulate Ctrl+C and return clipboard contents."""
    with kbd.pressed(Key.ctrl):
        kbd.press('c')
        kbd.release('c')
    time.sleep(0.1)  # give clipboard time to update
    return pyperclip.paste()

def click_loop():
    global clicking
    while clicking:
        press_time = random.uniform(*RELEASE_DELAY_MS) / 1000.0  # convert to seconds
        total_delay = random.uniform(DELAY_MS - DELAY_DELTA_MS, DELAY_MS + DELAY_DELTA_MS) / 1000.0
        release_time = total_delay - press_time

        mouse.press(Button.left)
        time.sleep(press_time)
        mouse.release(Button.left)
        time.sleep(max(release_time, 0))
    
        copied_text = copy_clipboard()
        if TARGET_STRING in copied_text:
            print(f"[INFO] Found target string: '{TARGET_STRING}'. Stopping.")
            clicking = False
            break

def on_press(key):
    global clicking, click_thread

    if isinstance(key, KeyCode):
        if key.char == START_KEY and not clicking:
            clicking = True
            click_thread = threading.Thread(target=click_loop)
            click_thread.start()

        elif key.char == END_KEY and clicking:
            clicking = False
            click_thread.join()
        
        elif key.char == EXIT_KEY:
            if clicking:
                clicking = False
                click_thread.join()
            exit()

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
