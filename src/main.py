from http.client import HTTPException
from fastapi import FastAPI, Depends, Header
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Api demo",
              description="API demo for GCP.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok"}


