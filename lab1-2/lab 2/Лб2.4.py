print('Пусть дана строка:\n')
l = 'Stydent 2 kyrsa Gruppa BST1703 Fakultet OTF2'
print(l)
new_str1 = ''
new_str2 = ''
for i in l:
    if i.isalpha():
        new_str1 += i
    if i.isdigit():
        new_str2 += i
print('\nСтрока из букв:\n ' + new_str1)
print('\nСтрока из цифр:\n ' + new_str2)
input("\nНажмите Enter для выхода из програмы\n")