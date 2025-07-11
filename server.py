from fastapi import FastAPI, Header, HTTPException
from pynput.keyboard import Controller

app = FastAPI()
kbd = Controller()

secret = 'aaronwangwaggityfiveways'

def execute_response() -> None:
    """
    Called whenever we receive /ping.
    Presses the *Q* key once, then returns.
    """
    kbd.press('q')
    kbd.release('q')

@app.post("/ping")
def ping(x_token: str = Header(None)):
    if x_token != secret:
        raise HTTPException(status_code=401)
    execute_response()
    return {"status": "ok"}