import string
import random
some_str = ''
a = string.digits + string.ascii_lowercase 
print("Сгенерированная строка:\n ")
for i in range(8):
    some_str += random.choice(a)
print(some_str)
input("\nНажмите Enter для выхода из програмы\n")
