import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
APP_NAME = os.getenv("APP_NAME", "Temperature converter")
APP_AUTHOR = os.getenv("APP_AUTHOR", "Unknown")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(title=APP_NAME)


@app.get("/health")
def health():
    return {"status": "ok"}
