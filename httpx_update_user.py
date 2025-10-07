from traceback import print_tb

import httpx
from tools import fakers

user_data_payload = {
    "email": fakers.get_random_email(),
    "password": "12345",
    "lastName": "imasheva",
    "firstName": "albina",
    "middleName": "albertovna"
}

user_create_response = httpx.post("http://localhost:8000/api/v1/users", json=user_data_payload)
user_create_response_data = user_create_response.json()

print(user_create_response.status_code)
print(user_create_response_data)

user_login_payload = {
    "email": user_create_response_data['user']['email'],
    "password": "12345"
}

user_login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_login_payload)
user_login_response_data = user_login_response.json()

print(user_login_response.status_code)
print(user_login_response_data)

update_user_payload = {
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

headers = {"Authorization": f"Bearer {user_login_response_data['token']['accessToken']}"}

user_update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_create_response_data["user"]["id"]}",
                                   json=update_user_payload, headers=headers)

user_update_response_data = user_update_response.json()

print(user_update_response.status_code)
print(user_update_response_data)
