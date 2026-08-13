from httpx import Client

client = Client(base_url="http://localhost:8000")

payload = {
    "email": "user@example.com",
    "password": "string"

}

login_response = client.post('/api/v1/authentication/login', json=payload)
login_response_data = login_response.json()

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = client.post("/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print('Refresh response:', refresh_response_data)
print('Status code:', refresh_response.status_code)
print('Старое:', refresh_response.text)
