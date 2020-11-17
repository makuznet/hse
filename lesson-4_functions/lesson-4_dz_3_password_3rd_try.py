# Используя генератор паролей создайте свой.
#
# passwd = ''
# for x in range(12):
#     passwd += random.choice(
#         '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
# print(passwd)
#
# Пароли, получаемые в результате, должны удовлетворять следующим условиям:
#  - длина пароля - 15 символов
#  - в пароле есть 3 заглавные буквы (любые, в любом месте пароля)
#  - в пароле есть 4 цифры (любые, в любом месте)
#  - оставшиеся символы пароля - строчные латинские буквы

import random

passwd = ''
vocab = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'

while len(passwd) < 15:

    candidate = random.choice(vocab)

    # вычисляем количество символов каждого типа в пароле на текущем этапе
    lowcase = [symbol for symbol in passwd if symbol.islower()]
    capital = [symbol for symbol in passwd if symbol.isupper()]
    numbers = [symbol for symbol in passwd if symbol.isdigit()]

    # добавляем символ-кандидат в пароль,
    # если удовлетворяется одно из условий
    conditions = (
        candidate.islower() and len(lowcase) < 8,
        candidate.isupper() and len(capital) < 3,
        candidate.isdigit() and len(numbers) < 4
    )

    if any(conditions):
        passwd += candidate

print('\n', passwd, '\n')
