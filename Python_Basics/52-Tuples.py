# Tuple: it's like a mutable list

my_tuple = ('a','b','c','d','e')

# like lists, can be accessed by index numbers
print(my_tuple[2]) # c

# can be checked with booleans too
print('e' in my_tuple) # True

# Performs better than a list becuase of its immutability
## if you need a list that won't change, just use a Tuple 

# A Tuple is a valid key for a dict

user1 = {
  'name': 'Manuel',
  'last_name': 'Dorante',
  my_tuple: 23
}
print(user1) # {'name': 'Manuel', 'last_name': 'Dorante', ('a', 'b', 'c', 'd', 'e'): 23}