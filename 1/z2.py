minsum = 0
plussum = 0

i = int(input('Введите число: '))
for t in range(-i,i + 1):
    print('Число ', t);
    if t < 0:
        minsum += t;
    elif t > 0:
        plussum += t;
print("Сумма отрицательных: ", minsum);
print("Сумма положительных: ", plussum);
