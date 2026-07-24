from fastapi import FastAPI
from src.api.routers import companies

app = FastAPI(
    title="NIFTY100 Analytics API",
    description="REST API for NIFTY100 Financial Intelligence Platform",
    version="1.0.0"
)

app.include_router(companies.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to NIFTY100 Analytics API"
    }