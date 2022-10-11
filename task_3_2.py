import hashlib
from uuid import uuid4
password = input('введите пароль из латинских букв и цифр: ')
salt = uuid4().hex
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
file = open('passwd.csv', 'w')
file.write(res)
file.close()
while True:
    try:
        password_1 = input('введите пароль из латинских букв и цифр: ')
        res_1 = hashlib.sha256(salt.encode() + password_1.encode()).hexdigest()
    except TypeError:
        print('ошибка при вводе пароля')
    else:
        with open('passwd.csv') as f:
            if res_1 == f.readline():
                print('доступ разрешен!')
                break
            else:
                print('введен неправильный пароль')
