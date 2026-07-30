import json

new_user = {
    "name": "Мария",
    "age": 25,
    "is_student": False,
    "courses": ["ui", "api"],
    "address": {
        "city": "Москва",
        "street": "Ленина",
        "house": 14
    }
}

j_user = json.dumps(new_user, indent=4, ensure_ascii=False)

with open("new_j.json", "r", encoding="UTF-8") as file:
    new_file = json.load(file)


print(new_file['name'])