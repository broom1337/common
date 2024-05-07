
def format_error(err):
    if err.isdigit():
        err = int(err)
    if not isinstance(err, int):
            print('ValidationError: Неверный формат')
            exit()

def sum_calc(x: int,y: int):
    print(x+y)

def sub_calc(x: int,y: int):
    print(x-y)

def mul_calc(x: int,y: int):
    print(x*y)

def div_calc(x: int,y: int) -> float:
    if y == 0:
        raise ValueError("Деление на ноль")
    print(x/y)

def deg_calc(x: int, y: int):
    print(x**y)

def my_calc():
    print("""
          1. Сложение
          2. Вычитание
          3. Умножение
          4. Деление
          5. Возведение в степень  
          6. Выход    
          """)
    act = input("Выберите действие(введите число): ")
    format_error(act)
    if int(act) < 1 or int(act) > 6:
            print('Error: Неверный ввод данных')
            exit()
    act = int(act)
    
    if act != 6:
        a = input("1-е число: ")
        b = input("2-е число: ")
        format_error(a)
        format_error(b)
        a = int(a)
        b = int(b)
        print("Результат:")

    if act == 1:
        sum_calc(a,b)
    
    if act == 2:
        sub_calc(a,b)
    
    if act == 3:
        mul_calc(a,b)

    if act == 4:
        div_calc(a,b)

    if act == 5:
        deg_calc(a,b)
    
    if act != 6:
        print("Вернуться в меню (д/н)")
        r = input()
        if r != 'д' and r != 'н':
            print('Error: Неверный ввод данных')
            exit()
    
    if act == 6 or r == 'н':
        exit()
    
    if r == 'д':
        my_calc()

my_calc()
    