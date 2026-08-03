from importlib.metadata import files
from tkinter.scrolledtext import example

import httpx

# Получить информацию
response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())

# Создать информацию
data = {
    "title": "Новая задача",
    "completed": False,
    "userID": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.json())

data = {"username": "test_user", "password": "12345"}

# Data - когда нужно отправить строку
response = httpx.post("https://postman-echo.com/post", data=data)
# print(response.status_code)
# print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://postman-echo.com/get", headers=headers)


# print(response.request.headers)
# print(response.json())
params = {"userID": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://postman-echo.com/post", files=files)

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")


print(response1.json())
print(response2.json())

client.httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
