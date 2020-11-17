# Используя генератор паролей создайте свой.

# passwd = ''
# for x in range(12):
#     passwd += random.choice(
#         '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
# print(passwd)

# Пароли, получаемые в результате, должны удовлетворять следующим условиям:
#  - длина пароля - 15 символов
#  - в пароле есть 3 заглавные буквы (любые, в любом месте пароля)
#  - в пароле есть 4 цифры (любые, в любом месте)
#  - оставшиеся символы пароля - строчные латинские буквы


import random

passwd = []

while len(passwd) < 15:
    passwd.append(random.choice(
        'qwertyuiopasdfghjklzxcvbnm'))
# print(passwd)

for index in range(1, 12, 4):
    passwd[index] = passwd[index].replace(passwd[index], passwd[index].upper())
# print(passwd)

for index in range(14, 0, -4):
    passwd[index] = passwd[index].replace(
        passwd[index], random.choice('0123456789'))
# print(passwd)

capital = [symbol for symbol in passwd if symbol.isupper()]
numbers = [symbol for symbol in passwd if symbol.isdigit()]

print()
print('Your password is', end=' ')
[print(passwd[index], end='') for index in range(len(passwd))]
print()
print()

print(len(capital), 'capital letters in the password:', capital)
print(len(numbers), 'digits in the password:', numbers)
print('password length:', len(passwd))

# Пример работы кода:
#
# Your password is cN3bzG9trP7znb3
#
# 3 capital letters in the password: ['N', 'G', 'P']
# 4 digits in the password: ['3', '9', '7', '3']
# Password length: 15
