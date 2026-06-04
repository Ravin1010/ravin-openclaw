from fastapi import FastAPI
from backend.app.routes.chat import router as chat_router

app = FastAPI(title="OpenClaw API")

app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "OpenClaw backend running"}