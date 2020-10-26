#
# элементы в переменной text преобразуйте в нижний регистр,
# а затем запишите наоборот, с последнего элемента по первый
# text = "WOW,NOEL SEES LEON"
#
# HARD WAY: Используйте list comprehension
#

text = "WOW,NOEL SEES LEON"  # исходная строка

# text.split(',') создает список из элементов, используя запятую как разделитель
# цикл создает список списков, превращая каждый элемент text.split(',') в список

data = [row.split() for row in text.split(',')]

print()

# печатаем из конца в начало элемент каждой строки
# подстановку запятой осуществляем после печати нулевого элемента строки
# но не после нулевого элемента последней строки

[
    print(data[row][index], end=' ') if index != 0 or (row == index == 0)
    else print(data[row][index], end=', ')
    for row in range(len(data)-1, -1, -1)
    for index in range(len(data[row])-1, -1, -1)
]

print()
print()
