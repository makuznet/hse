# программа принимает с клавиатуры слова, записанные кириллицей,
# и печатает результат латиницей

# создаем функцию транслитерации с одним параметром
def translit_phrase(cyrillic_phrase):

    # создаем функцию по созданию словаря внутри функции транслитерации
    # это позволяет улучшать словарь независимо от функции транслитерации
    def translit_dict():
        translit = {}
        cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        latin = 'abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA'
        [translit.update({cyrillic[index]: latin[index]})
         for index in range(len(cyrillic))]
        return translit

    # вызываем функцию словаря для транслитерации
    # и передаем пользовательский ввод через параметр функции
    # сохраненный в переменной cyrillic_phrase с областью видимости внутри функции
    [print(translit_dict().get(index), end='') if index
     in translit_dict() else print(index, end='') for index in cyrillic_phrase]
    print()


# вызываем функцию транслитерации,
# передавая в качестве аргумента пользовательский ввод
translit_phrase(input('Введите текст для транслитерации: '))
