from fastapi import FastAPI, Header, HTTPException
from pynput.keyboard import Controller
import time
import random
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
kbd = Controller()
dash_key = 'q'

TOKEN = os.getenv("TOKEN")

def execute_response() -> None:
    """
    Called whenever we receive /ping.
    Presses the *Q* key once, then returns.
    """
    time.sleep(random.uniform(0.010, 0.040))
    kbd.press(dash_key)
    time.sleep(random.uniform(0.040, 0.060))
    kbd.release(dash_key)

@app.post("/ping")
def ping(x_token: str = Header(None)):
    if x_token != TOKEN:
        raise HTTPException(status_code=401)
    execute_response()
    return {"status": "ok"}