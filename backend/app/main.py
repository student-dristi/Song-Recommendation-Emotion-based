from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import emotion

app = FastAPI(title="Emotion2Music - Dev Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(emotion.router, prefix="/api")

