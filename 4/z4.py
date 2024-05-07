def decorator(func):
    def args(*args, **kwargs):
        print(f'Была вызвана функция {func.__name__} с аргументами {args, kwargs}')
        return func(*args, **kwargs)
    return args

@decorator
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