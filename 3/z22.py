
lam_list_mul = lambda l, ch = None: [i*ch if ch is not None else i*2 for i in l]


count = int(input('Число элементов списка: '))

my_list = []

for i in range(count):
    el = int(input(f"Число {i+1} списка: "))
    my_list.append(el)

my_number = int(input('Введите число, на которое умножится каждый элемент списка: '))

print('Список пользователя:')
print(lam_list_mul(my_list, my_number))
print('Список без ввода числа:')
print(lam_list_mul(my_list))