from fastapi import APIRouter
from app.scraper import fetch_page

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Week 5 scraper is running successfully"
    }
    
@router.get("/health")
def root():
    return {
        "status": "healthy"
    }
    
@router.get("/scrape")
def scrape():
    
    url = "https://books.toscrape.com"
    
    return fetch_page(url)