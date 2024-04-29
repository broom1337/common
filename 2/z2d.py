# Задание 2*

set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

set12u = set1 | set2
set123u = set12u | set3
set12c = set1 & set2
set23c = set2 & set3
set13c = set1 & set3
setcombined = set12c | set23c | set13c
setdiff = set123u - setcombined

print (f'Объединение 1 и 2: {set12u}')
print (f'Объединение 1, 2 и 3: {set123u}')
print (f'"Пропавшие элементы": {setcombined}')
print (f'Разница всех элементов множества и списка: {setdiff}')