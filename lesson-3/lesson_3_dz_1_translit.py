# программа принимает с клавиатуры слова, записанные кириллицей,
# и печатает результат латиницей
translit = {}
cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
latin = 'abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA'
[translit.update({bukva: letter}) for bukva in cyrillic for letter in latin]
print(translit)
# translit = {'е': '2', 'п': '3'}
# cyrillic = input('Введите текст для транслитерации: ')
# [print(translit.get(index), end='') if index
#  in translit else print(index, end='') for index in cyrillic]
# print()
