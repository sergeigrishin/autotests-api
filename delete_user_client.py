from randon_random import email_random
from httpx import Client

client = Client(base_url="http://localhost:8000")
create_user_payload = {
    "email": email_random(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_new_user_response = client.post('/api/v1/users', json=create_user_payload)
create_new_user_response_data = create_new_user_response.json()
print('1) Пользователь создан:', create_new_user_response_data)
print()
###############################################################################
login_client_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password'],
}
authentic_user_response = client.post('/api/v1/authentication/login', json=login_client_payload)
authentic_user_response_data = authentic_user_response.json()
print('2) Пользователь авторизован', authentic_user_response_data)

token_user = {
    "Authorization": f"Bearer {authentic_user_response_data['token']['accessToken']}"
}

new_payload = {
      "email": email_random(),
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }

update_user_response = client.patch(f"/api/v1/users/{create_new_user_response_data['user']['id']}",headers=token_user ,json=new_payload)
update_user_response_date = update_user_response.json()
print()
print('3)Данные обновлены:', update_user_response_date)
