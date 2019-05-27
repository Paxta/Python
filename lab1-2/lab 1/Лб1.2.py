l = list(input('Введите строку:\n'))
string = ""
print('Элементы которые находяться на нечетной позиции строки:')
for i in range(0,len(l)):
    if i % 2 == 0:
        string = string + l[i]+" "
print(string)
input("Нажмите Enter для выхода из програмы\n")