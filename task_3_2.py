import hashlib
from uuid import uuid4
salt = uuid4().hex
def create_hash():
    password = input('введите пароль из латинских букв и цифр: ')
    res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    return res
res = create_hash()   
file = open('passwd.csv', 'w')
file.write(res)
file.close()
while True:
    try:
        res_1 = create_hash()
    except TypeError:
        print('ошибка при вводе пароля')
    else:
        with open('passwd.csv') as f:
            if res_1 == f.readline():
                print('доступ разрешен!')
                break
            else:
                print('введен неправильный пароль')
