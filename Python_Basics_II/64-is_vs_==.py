# is vs ==

# == checks equality of values
print(True == 1) # True ## the 1 gets converted to bool for comparison and it's a Truthy value
print('1' == 1) # False ## the first is a string, the second is an integer
print([] == 1) # False
print(10 == 10.0) # True ## the 10.0 gets converted to an int for comparison and 10 == 10 returns True
print([] == []) # True

print()

#is checks if the memory location for the values is the same
print(True is 1) # False
print('1' is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # False

print()

print(True is True) # True
print('1' is '1') # True
print([] is []) # False, because every list is created in it's own memory location, even if it's the same as an already existing one
print([1,2,3] is [1,2,3]) # False

print()

a = 12345
b = 12345
print( a is b) # True, in this case, both a and b point to the same location in memory

print()

c = 'hey'
d = 'hey'
print( c is d) # True, in this case c and d also point to the same location in memory