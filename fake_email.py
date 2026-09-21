import time

def fake_email():
    return f'{time.time()}@email.ru'


print(fake_email())
