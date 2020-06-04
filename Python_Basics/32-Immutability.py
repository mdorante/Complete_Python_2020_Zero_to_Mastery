# Immutability

# Once a string is created, I can't modify pieces of it

numbers = '0123455678'
print(numbers)
print()
#Doing something like numbers[0] = 7 would cause an error

#I can only change the whole value of the variable
numbers = '012345'
print(numbers)
print()

# Or I can modify it using expressions
numbers = numbers + numbers[0] # '012345' + '0' 
print(numbers) #0123450