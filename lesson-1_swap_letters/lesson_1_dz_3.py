orange = 'апельсин'
# создаем слово "спаниель" из слова "апельсин" с помощью срезов"
print() # воздух для лучшей читаемости
print(orange[5], end='') # печатаем "с", 6 буква, индекс 5
print(orange[1::-1], end='') # печатаем "ап" в обратном порядке (-1) — "па" , с 1 индекса до начала, то есть, до 0 (индекс не задан)  
print(orange[:5:-1], end='') # печатаем "ин" в обратном порядке (-1) — "ни" , с 7 (индекс не указан) до 6 (5 не включяя) 
print(orange[2:5]) # печатаем "ель" со 2 по 4 (5 не включая)
print() # воздух для лучшей читаемости