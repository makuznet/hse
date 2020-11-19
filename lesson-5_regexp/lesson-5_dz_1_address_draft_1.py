import os
import re
path = os.path.dirname(os.path.abspath(__file__)) + '/addresses.txt'

with open(path, 'r') as f:
    for line in f:
        try:
            print(re.search(r'\d{3,4}(\ [A-Z].+){2,3}', line).group())
        except:
            result = None
        try:
            print(re.search(r'(Suite)\s\d{1,4}', line).group())
        except:
            result = None
        try:
            print(re.search(r'[A-Z].+\,\s[A-Z]{2}\ \d{5}', line).group(), '\n')
        except:
            result = None
f.close()
