# Use comprehensions to print out a list with only the duplicate elements from this list

list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({char for char in list1 if list1.count(char) > 1})
print(duplicates)  # ['n', 'b']
