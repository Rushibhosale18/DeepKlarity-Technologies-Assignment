import requests
from bs4 import BeautifulSoup
url = "https://minimalistbaker.com/easy-vegan-fried-rice/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
res = requests.get(url, headers=headers)
print("Status:", res.status_code)
if res.status_code == 200:
    print("Content length:", len(res.text))
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.get_text()[:200])
