import os
import re
path = os.path.dirname(os.path.abspath(__file__)) + '/addresses.txt'

with open(path, 'r') as f:
    lines = f.readlines()
f.close()

for line in lines:

    conditions = (
        re.search(r'\d{3,4}(\ [A-Z].+){2,3}', line) != None,
        re.search(r'(Suite)\s\d{1,4}', line) != None,
        re.search(r'[A-Z].+\,\s[A-Z]{2}\ \d{5}', line) != None
    )

    if any(conditions):
        print(line, end='')
