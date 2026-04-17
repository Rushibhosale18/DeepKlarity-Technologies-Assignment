import requests

url = "http://localhost:8001/api/extract"
payload = {"url": "https://minimalistbaker.com/easy-vegan-fried-rice/"}

try:
    print("Sending POST request to LOCAL backend...")
    response = requests.post(url, json=payload, timeout=30)
    print("Status code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except:
        print("Response text:", response.text)
except Exception as e:
    print("Error:", e)
