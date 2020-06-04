# Dictionary: Un-ordered key-value pair

# It is a data type and also a data structure (like a list is a data type but also a data structure)

# It's contents have keys and values, for example:

dictionary = {
  'a': 1, # a is the key, with a value of 1
  'b': 2
} #Notice curly brackets, not square brackets

print(dictionary) # {'a': 1, 'b': 2}

# Items don't have to be in order and don't have to be the same data types

dictionary2 = {
  'a': [1,2,3],
  'u': 'Wassup',
  'b': True 
}
print(dictionary2) # 'a': [1, 2, 3], 'u': 'Wassup', 'b': True}

print(dictionary2['a']) # [1, 2, 3]

print(dictionary2['a'][1]) # 2

# Lists can contain dictionaries as well
list1 = [ 
  {
  'a': [1,2,3],
  'u': 'Wassup',
  'b': True 
  },
  {
  'a': [4,5,6],
  'u': 'Wassup',
  'b': True 
  }
]

print(list1[0]['a'][2]) # 3

print(list1[1]['u'][0]) # W

