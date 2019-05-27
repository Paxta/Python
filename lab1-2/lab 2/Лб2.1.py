import random
my_number = random.randint(1,10000)
user_number = 0
while my_number >= user_number:
    user_number = int(input('user_number: '))
print('Рандомно загаданное число число: ' + str(my_number))
input('Нажмите Enter для выхода из программы\n')