import requests
url = "http://127.0.0.1:5000/predict"
data = {
    "texts": ["Bist Du krank?", 
              "Hello, my friends!",
              "Delft is mijn tweede woonplaats"]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Predictions:", response.json())
else:
    print("Error:", response.status_code, response.text)
