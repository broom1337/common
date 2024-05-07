

i = input()


if len(i) == 3 and i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
    print(i[0] + i[1] + i[2])
    print(i[0] + i[2] + i[1])
    print(i[1] + i[0] + i[2])
    print(i[1] + i[2] + i[0])
    print(i[2] + i[0] + i[1])
    print(i[2] + i[1] + i[0])
else:
    print('Incorrect')
