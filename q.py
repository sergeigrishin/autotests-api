response = {
    "status": "success",
    "users": [
        {"id": 1, "name": "Ivan"},
        {"id": 2, "name": "Anna"}
    ]
}

def validate_response(response):
    if response['status'] != 'success':
        return False
    if response['users'] is None:
        return False
    for v in response['users']:
        if "id" and "name" not in v:
            return False
    return True



print(validate_response(response))