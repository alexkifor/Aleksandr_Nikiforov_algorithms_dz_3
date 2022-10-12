import hashlib
сash = {'ya.ru': 'afcb4329d72e4e1c4ff20792c11c5221f29089ce212748782ef2e84f845ca027'}
salt = 'my_salt'
def check_url(url):
    if url in сash.keys():
        return f'хэш {url} - {сash[url]}'
    else:
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        сash.setdefault(url, hash_url)
        return f'{url} добавлен в кэш'


print(check_url('ya.ru'))
print(check_url('gb.ru'))
print(сash)
