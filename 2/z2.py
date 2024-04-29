
input = input('Введите строку: ')

slovar = {}

for i in input:
    if i != ' ':
        i = i.lower()
        sum = input.count(i)
        slovar[i] = sum

print(slovar)