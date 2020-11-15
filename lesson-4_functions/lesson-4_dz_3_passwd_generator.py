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

# импортируем модуль случайного выбора
import random

# пустая переменная для хранения пароля
passwd = ''
# три заглавные буквы
[passwd := passwd + (random.choice('qwertyuiopasdfghjklzxcvbnm')
                     ).capitalize() for any in range(3)]
# четыре цифры
[passwd := passwd + random.choice('0123456789') for any in range(4)]
# и строчные буквы
[passwd := passwd + random.choice('qwertyuiopasdfghjklzxcvbnm')
 for any in range(8)]
# перемешиваем и выводим пароль из 15 символов
print(''.join(random.sample(passwd, len(passwd))))
