import requests

url = "http://127.0.0.1:8000/items/"

item = {
    "id": 2,
    "name": "ciao",
    "description": "yolo",
    "price": 50,
    "tax": 2.5
}

response = requests.post(url, json=item)
print(response.json())