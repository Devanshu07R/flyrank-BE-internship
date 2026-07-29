import requests
import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin 
from bs4 import BeautifulSoup
import json

USER_AGENT = "FlyRank-Backend-Internship/1.0 (Devanshu Dasgupta)"

def can_fetch(url: str):
    rp = RobotFileParser()
    rp.set_url(urljoin(url, "/robots.txt"))
    rp.read()
    
    return rp.can_fetch(USER_AGENT, url)
    
def fetch_page(url: str):
    
    if not can_fetch(url):
    
        return {
            "status": "blocked",
            "message": "robots.txt does not allow scraping"
        }
        
    headers = {
            "User-Agent": USER_AGENT
        }
        #polite delay
    time.sleep(1)
        
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "lxml")
    
    books = []
    
    for book in soup.find_all("article", class_ = "product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()
        rating = book.p["class"][1]
        
        books.append(
            {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating
            }
        )
    with open("books.json", "w", encoding="utf-8") as file:
          json.dump(books, file, indent=4, ensure_ascii=False)
    return {
            "status": response.status_code,
            "count": len(books),
            "books": books
        }