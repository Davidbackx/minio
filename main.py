from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/log")
def log():
    with open("log.txt", "a+") as f:
        f.write("Log\n")
        f.seek(0)  # Go to the start of the file before reading
        lines = f.readlines()
    return {"Log": lines}

@app.get("/hello")
def hello():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
