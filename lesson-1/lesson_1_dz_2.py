print() # some air for usability
data = ['there is nothing good or bad in it', 'but thinking makes it so', 'for me Denmark is prison'] #my data

print(data[0], data[1], data[2]) # method 1, commas put spaces
print()
 
for phrase in data: 
    print(phrase, end=' ') # method 2, printing list elements one by one, appending to the string with end= keyword 
print()
print()

for counter in range(len(data)): 
   print(data[counter], end=' ') # method 3, printing by calling an element number, appending with end= keyword
print()
print()