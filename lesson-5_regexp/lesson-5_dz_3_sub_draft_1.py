# замените все вхождения слова "морж" на слово "корж"

import os
import re

# абсолютный путь к файлу
path = os.path.dirname(os.path.abspath(__file__)) + '/морж-корж.txt'

# для каждой строки производим замену и выводим на печать
for line in open(path):
    line = re.sub('Морж', 'Корж', line)
    line = re.sub('морж', 'корж', line)
    print(line)
