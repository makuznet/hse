# Напишите код, который проверяет делимость числа на 5.
# Числа нужно выбрать из списка. Если число делится,
# алгоритм должен выйти из цикла и вывести на экран искомое число и строку "делится на 5".
# Если не делится, выводим на экран "это не делится на 5, продолжим поиск".
# Продолжаем пока не найдем такое, которое бы делилось.
# Проверяя числа на делимость, алгоритм также должен игнорировать число 45, не прервав на нем цикл.

numbers = [2, 6, 7, 45, 1, 89, 678, 35, 11]

for element in numbers:
    if element % 5 != 0:
        print(element, 'не делится на 5. Продолжаем поиск!')
    elif element % 5 == 0 and element == 45:
        print(element, 'делится на 5. Игнорируем!')
    elif element % 5 == 0:
        print(element, 'делится на 5. Поиск прерван.')
        break
print()
