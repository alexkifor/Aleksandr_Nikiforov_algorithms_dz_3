from time import perf_counter
# a)
def check_time(func):
    def inner(*args):
        start = perf_counter()
        my_func = func(*args)
        end = perf_counter()
        print(f'время выполнения функции {end - start} сек.')
        return my_func
    return inner

@check_time
def create_list(n):
    list = []
    for i in range(n):
        list.append(i)
    return list
# Сложность функции O(n)

@check_time
def create_dict(n):
    dict = {}
    for i in range(n):
        dict[i] = i
    return dict
# Сложность функции O(n)

list_1 = create_list(1000)
dict_1 = create_dict(1000)
print(list_1)
print(dict_1)

# При одинаковой сложности, функция по заполнению списка работает примерно в 1,5 раза быстрее

# b)

@check_time
def get_elem_list(list, n):
    for i in range(len(list)):   #O(n)
        if i == n:               #O(1)
            return list[i]       #O(1)
# Сложность функции O(n)

@check_time
def get_elem_dict(dict, n):
    for i in range(len(dict.keys())):    #O(n)
        if i == n:                       #O(1)
            return dict[i]               #O(1)
# Сложность функции O(n)

print(get_elem_dict(dict_1, 100))
print(get_elem_list(list_1, 100))
# Получение элемента списка происходит медленне, чем у словаря

# c)
@check_time
def del_elem_list(list, n):
    for i in range(len(list)):      #O(n)
        if i == n:                  #O(1)
            list.pop(i)             #O(n)
            return list
#Сложность функции O(n**2)

@check_time
def del_elem_dict(dict, n):
    for i in range(len(dict.keys())):  #O(n)
        if i == n:                     #O(1)
            dict.pop(i)                #O(1)
            return dict                #O(1)

#Сложность функции O(n)

print(del_elem_dict(dict_1, 13))
print(del_elem_list(list_1, 13))

#Удаление элемента у словаря происходит быстрее, т.к. метод pop словаря имеет сложность O(1), против O(1) у словаря

