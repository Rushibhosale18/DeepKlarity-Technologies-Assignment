import urllib.request
import json

url = "https://deepklarity-technologies-assignment.onrender.com/api/recipes"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f"Total recipes: {len(data)}")
        if len(data) > 0:
            print("Latest recipe keys:", data[-1].keys())
            print("Has nutrition_estimate?", 'nutrition_estimate' in data[-1])
            if 'nutrition_estimate' in data[-1]:
                print("nutrition_estimate looks like:", data[-1]['nutrition_estimate'])
            else:
                print("Full data:", data[-1])
except Exception as e:
    print("Error:", e)
