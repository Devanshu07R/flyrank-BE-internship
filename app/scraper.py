import requests
import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin 

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
        
    return {
            "status": response.status_code,
            "html": response.text
        }