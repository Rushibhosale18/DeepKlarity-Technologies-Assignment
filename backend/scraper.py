import requests
from bs4 import BeautifulSoup

def scrape_recipe(url: str):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text(separator="\n")
        return text[:15000]
    except Exception:
        return None