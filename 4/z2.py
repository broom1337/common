

def fib_gen(num):
    if num == 0:
        print('Пустое множество')
    x, y = 1, 1
    for space in range(num):
        yield x 
        x, y = y, x + y

num = int(input("Введите количество чисел Фибоначчи: "))

for i in fib_gen(num):
    print(i)