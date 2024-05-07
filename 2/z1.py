
try:
    am = int(input('Введите количество чисел списка: '))
except ValueError:
    print('Ошибка: Введите численное значение')
    exit()
    
listnum = []
listpow = []

for i in range(am):
    number = input(f'Введите {i+1}-е число: ')
    listnum.append(number)
    try:
        power = int(input('Введите количество чисел списка: '))
    except ValueError:
        print('Ошибка: Введите численное значение')
        exit()
    listpow.append(power)

for t in range(len(listnum)):
    number = listnum[t]
    power = listpow[t]

    if number.isdigit():
        number = int(number)
        print(f'{number} в степени {power} = {number**power}')

    elif number[0] == '-' and number[1:].isdigit():
        number = int(number)
        print(f'{number} в степени {power} = {number**power}')

    else:
        print(f'{number} в повторении {power} = {number * power}')