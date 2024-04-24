
while True:
    i = input("Введите положительное число: ")
    if i == 'exit':
        break
    if i.isdigit():
        print(len(i));
    else:
        print('Это не положительное число')
        


