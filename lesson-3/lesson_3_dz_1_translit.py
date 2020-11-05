# программа принимает с клавиатуры слова, записанные кириллицей,
# и печатает результат латиницей
translit = {'е': '2', 'п': '3'}
cyrillic = input('Введите текст для транслитерации: ')
# [print(index, end='') for index in cyrillic]
# print()
[print(translit.get(index), end='') for index in cyrillic]
print()
