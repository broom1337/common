
def file_edit(text,name):
    with open(name, 'a+', encoding='utf-8') as file:
        file.write(f'\n{text}')

text = input("Введите текст для дополнения файла: ")
name = input("Введите имя файла: ")

file_edit(text,name)

def even(name):
    with open(name, 'r', encoding='utf-8') as file:
        readlines = file.readlines()
        for i in range(1,len(readlines),2):
            print(readlines[i])
print('Вывод четных строк:')
even(name)
