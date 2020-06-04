# More Dictionary Methods

user = {
  'numbers': [1,2,3,4,5,6],
  'greet': 'Hi',
  'age': 20
}

# .keys() -> returns the keys
print(user.keys()) # dict_keys(['numbers', 'greet', 'age'])

print('size' in user.keys()) # False
print('age' in user.keys()) # True

# .values() -> returns the key values
print(user.values()) # dict_values([[1, 2, 3, 4, 5, 6], 'Hi', 20])

print(20 in user.values()) # True
print('password' in user.values()) # False

# .items() -> returns key-value pairs
print(user.items()) # dict_items([('numbers', [1, 2, 3, 4, 5, 6]), ('greet', 'Hi'), ('age', 20)])

# .clear() -> removes all items from the dictionary [in-place]
user.clear()
print(user) # {}

user2 = {
  'name': 'Manuel',
  'last_name': 'Dorante',
  'age': 23,
  'is_cool': True
}

# .copy() -> creates a copy of the dict
user3 = user2.copy()
print(user2) # {'name': 'Manuel', 'last_name': 'Dorante', 'age': 23, 'is_cool': True}
print(user3) # {'name': 'Manuel', 'last_name': 'Dorante', 'age': 23, 'is_cool': True}

# .popitem() -> removes the item that was last inserted into the dictionary
print(user3.popitem()) # ('is_cool', True) ##this is the item that was just removed
print(user3) # {'name': 'Manuel', 'last_name': 'Dorante', 'age': 23} ##note that the 'is_cool' key-value pair was removed

# .update() -> modifies an existing key's value or adds a key-value pair if the key doesn't already exist in the dict
user3.update({'age': 34})
print(user3) # {'name': 'Manuel', 'last_name': 'Dorante', 'age': 34} ##note that age was modified to 34

user3.update({'number': 11})
print(user3) # {'name': 'Manuel', 'last_name': 'Dorante', 'age': 34, 'number': 11} ##note that the item 'number' was added
