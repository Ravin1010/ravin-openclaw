from fastapi import FastAPI

app = FastAPI(title="OpenClaw API")


@app.get("/")
def root():
    return {"message": "OpenClaw backend running"}