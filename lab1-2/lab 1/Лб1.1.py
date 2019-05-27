a = float(input("Введите a: "))
if a==0:
    while a==0:
        print('Ошибка будет деление на ноль: ')
        a = float(input("Введите a не равную 0: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
f = float(input("Введите f: "))
z = abs(a-b*c*pow(d,3)+(pow(c,5)-pow(a,2))/a +pow(f,3)*(a-213))
print('Ответ: ' + str(z))
input("Нажмите Enter для выхода из програмы\n")