# Dictionary Methods

user = {
  'basket': [1,2,3,4,5],
  'greeting': 'wassup'
}

# .get() -> returns the value of a key if it exists, (None if the key doesn't exist)
print(user.get('basket')) # [1, 2, 3, 4, 5]

# a default value can be set for use if the key doesn't exist
print(user.get('age', 34)) #returns '34', because the key 'age' doesn't exist
#NOTE: it doesn't actually modify the dict
print(user)
print()

# .dict() -> can be used to create a new dictionary [in-place]

user2 = dict(name='Manuel',last_name='Dorante')
print(user2) # {'name': 'Manuel', 'last_name': 'Dorante'}

