# Logical Operators

# greater than >
print(4 > 5) # False
print('a' > 'b') # False, because the values compared are the ASCII table values and in ASCII, a = 97 and b = 98

# equals ==
##NOTE: = is used for assigning values, == is used for comparing values
print('hello' == 'hello') # True
print(5 == 8) # False

# less than <
print(1 < 5) # True

# You can do multiple comparisons in one single expression
print(1 < 2 < 3 < 4 < 5) # True
print(10 > 9 > 8 < 20 > 5) # False

# greater than or equal to >=
print(3 >= 2) # True
print(5 >= 5) # True

# less than or equal to <=
print(1 <= 4) # True
print(10 <= 10) # True

# not equal to !=
print(1 != 9) # True
print(5 != 5) # False

# not: a keyword that negates whatever expression follows
## is also a function

print(not True) # False
print(not(False)) # True