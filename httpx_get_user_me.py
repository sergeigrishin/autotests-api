from httpx import Client

client = Client(base_url="http://localhost:8000")

#1 код
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = client.post("/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)

token_response_login = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

get_me_response = client.get("/api/v1/users/me", headers=token_response_login)
get_user_response_data = get_me_response.json()
print("Get user response:", get_user_response_data)
print("Get user status code:", get_me_response.status_code)


