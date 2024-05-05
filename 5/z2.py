import calendar as cldr
import re

def cldrm(year: int,month: int):
    print(cldr.month(year,month))

def match(number):
    if number.startswith('+7'):
        print(re.match('^\\+7',number))
    else:
        print(re.match('^[78]',number))

y = int(input("Введите год: "))
m = int(input("Введите месяц: "))
t = input("Введите номер телефона: ")

cldrm(y,m)
match(t)