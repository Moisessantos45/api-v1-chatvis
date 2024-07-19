from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers.public import public_router

app = FastAPI()
origns = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origns,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
    ],
    allow_headers=["*"],
)

app.include_router(public_router, prefix="/api/chatvis/v1")
