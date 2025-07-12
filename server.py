from fastapi import FastAPI, Header, HTTPException
from pynput.keyboard import Controller
import time
import random

app = FastAPI()
kbd = Controller()
dash_key = 'q'

secret = ''

def execute_response() -> None:
    """
    Called whenever we receive /ping.
    Presses the *Q* key once, then returns.
    """
    time.sleep(random.uniform(0.020, 0.100))
    kbd.press(dash_key)
    time.sleep(random.uniform(0.020, 0.100))
    kbd.release(dash_key)

@app.post("/ping")
def ping(x_token: str = Header(None)):
    if x_token != secret:
        raise HTTPException(status_code=401)
    execute_response()
    return {"status": "ok"}