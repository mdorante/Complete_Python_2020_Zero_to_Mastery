#Formatted Strings

name = 'Manuel'
age = 23

print('Hi ' + name + ' you are ' + str(age) + ' years old')

#The same print sentence can be simplified with a formatted string
# f'string'
print(f'Hi {name} you are {age} years old')

# .format() can be used for place holders (like in C#)
print('Hi {0} you are {1} years old'.format(name, age))

# New variables can be created inside format()
print('Hi {new_name} you are {age} years old'.format(new_name = 'Naruto', age = 16))