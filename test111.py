import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


response = requests.get(f"{BASE_URL}/users")
content_type = response.headers['Connection']
print(response.text)
print(content_type)
print(response)

