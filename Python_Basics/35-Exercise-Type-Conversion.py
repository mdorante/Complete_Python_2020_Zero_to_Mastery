# Quick program that asks birth year and then displays your age

birth_year = int(input('What year were you born in?')) #converting user input (str) to an int in order to enable math operations with this variable

age = 2019 - birth_year

print(f'Your age is: {age}')