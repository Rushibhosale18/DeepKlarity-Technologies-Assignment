import requests
url = "https://www.allrecipes.com/recipe/23891/grilled-cheese-sandwich/"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    print("Status:", response.status_code)
except Exception as e:
    print("Error:", e)
