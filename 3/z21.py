
def list_mul(l: list, ch: int = None) -> list:
    if ch is None:
        ch = 2
    l2 = []
    for i in l:
        i = i*ch
        l2.append(i)
    return l2


count = int(input('Число элементов списка: '))

my_list = []

for i in range(count):
    el = int(input(f"Число {i+1} списка: "))
    my_list.append(el)

my_number = int(input('Введите число, на которое умножится каждый элемент списка: '))

print('Список пользователя:')
print(list_mul(my_list, my_number))
print('Список без ввода числа:')
print(list_mul(my_list))