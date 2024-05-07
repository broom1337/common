# Вариант 2
import random

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]

def rdch2(list: list):
    for i in range(2):
        print(random.choices(list))

rdch2(list_el)