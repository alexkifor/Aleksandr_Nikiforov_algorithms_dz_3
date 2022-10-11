s = input('Введите строку: ')
set_res = set()
dict_res = {}
for i in range(len(s)):
        for j in range(i + 1, len(s) if i == 0 else len(s) + 1):
            set_res.add(hash(s[i:j]))
            dict_res[s[i:j]] = hash(s[i:j])

print(f'Количество подстрок в строке {s} равно {len(set_res)}')
print(list(dict_res.keys()))




