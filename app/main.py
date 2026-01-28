from fastapi import FastAPI
from app.routes import router
from app.config import APP_NAME
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Age Calculator API is running"}
