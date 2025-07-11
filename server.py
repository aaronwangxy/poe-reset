from fastapi import FastAPI

app = FastAPI()

def execute_response():
    # Put actual logic here
    pass

@app.post("/ping")
def ping():
    print("Ping received")
    execute_response()
