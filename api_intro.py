import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print("Статус код:", response.status_code)
print("Количество пользователей:", len(response.json()))
print("Первый пользователь:", response.json()[0]["name"])

print(type(response.text))   # <class 'str'>
print(type(response.json())) # <class 'list'>
print(response.text)