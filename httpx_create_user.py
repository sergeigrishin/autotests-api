from httpx import Client
from randon_random import email_random

client = Client(base_url="http://localhost:8000")
payload = {
    "email": email_random(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = client.post('/api/v1/users', json=payload)
create_user_response_data = create_user_response.json()
print(create_user_response_data)
print('______________________________________')

login_payload = {
    "email": payload["email"],
    "password": payload["password"]
}
authentication_user = client.post('/api/v1/authentication/login', json=login_payload)
authentication_user_data = authentication_user.json()
print('Login data:', authentication_user_data)


token_user = {
"Authorization": f"Bearer {authentication_user_data['token']['accessToken']}"
}

get_user_response = client.get(f"/api/v1/users/{create_user_response_data['user']['id']}", headers=token_user)
get_user_response_d = get_user_response.json()
print('__________________________________________')
print('Get get_user data', get_user_response_d)