user_input = input('Введите число или текст: ') # любой ввод — это строка
try:
    value = int(user_input) # если с клавиатуры вводить a = 5, Питон сразу преобразует тип переменной в int
    print(value, '— целое число!')
    print('+, -, х, % — да! Конкатенация — нет!')
except ValueError:
    try:
        value = float(user_input) # если c клавиатуры вводить b = 2.66, Питон сразу преобразует тип во float
        print(value, '— число с дробной частью?!')
        print('+, -, х, % — да! Конкатенация — нет!')
    except ValueError:
        print('Это текст! Его можно конкатенировать с другим текстом.')  
        print('Например, трехкратно повторить:', user_input * 3) # трехкратно конкатенируем введенную строку