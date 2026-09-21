import httpx
from fake_email import fake_email

default_user = {
    "email": fake_email(),
    "password": "password",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

def test_create_file():
    registration_user_response = httpx.post("http://localhost:8000/api/v1/users", json=default_user)
    registration_user_response_data = registration_user_response.json()
    print(registration_user_response_data)

    authentication_user = {
        "email": default_user['email'],
        "password": default_user['password']
    }
    authentication_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=authentication_user)
    authentication_user_response_data = authentication_user_response.json()
    print(authentication_user_response_data)


    create_file_header = {
        "Authorization": f"Bearer {authentication_user_response_data['token']['accessToken']}"
    }

    create_file = httpx.post('http://localhost:8000/api/v1/files',
                             data={
                                "filename": "image.jpg",
                                "directory": "courses"},
                             files={
                                 "upload_file": open('./testdata/files/image.jpg', 'rb')
                                    },
                             headers=create_file_header
                             )


    create_file_data = create_file.json()
    print('Файл создан:', create_file_data)

