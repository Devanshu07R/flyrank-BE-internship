from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title = "Week 5 - Polite Scraper",
    version = "1.0"
)

app.include_router(router)