import random
l = []
string =""
for i in range(0,random.randint(5,20)):
    l.append(random.randint(-100,100))  
print('Числа в масиве: ' + str(l))
print('Число, находящееся посередине массива = ' + str(l[len(l)//2]))
input("Нажмите Enter для выхода из програмы\n")
