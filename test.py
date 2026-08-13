from httpx import Client


client = Client(base_url="http://localhost:8000", timeout=100)

user_authentication = {
    "email": "user@example.com",
    "password": "string"
}


response = client.post("/api/v1/autentication/login", json=user_authentication)
user_me_response_data = response.json()

print(user_me_response_data)