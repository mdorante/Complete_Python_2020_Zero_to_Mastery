# Exercise: Check for duplicates in list: (print only the letters that have duplicates)
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for letter in some_list:
  repeat = some_list.count(letter)
  if repeat > 1 and letter not in duplicates:
    duplicates.append(letter)
print(duplicates) # ['b', 'n']