# Iterables - list, dictionary, tuple, set, string
# iterate -> go one by one to check each item in the collection

# Let's see what happens if you want to iterate over a Dictionary
user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for item in user:
  print(item)
#Output:
# name
# age
# can_swim

# Only the keys are being checked, that's because we need to use some dictionary methods in order to access all the info we need

print()

# .items() will return the key-value pairs in tuples
for item in user.items():
  print(item)
#Output:
# ('name', 'Golem')
# ('age', 5006)
# ('can_swim', False)

print()

# .values() will return only the values
for item in user.values():
  print(item)
#Output:
# Golem
# 5006
# False

print()

# .keys() will return only the keys (like using the name of the dict without any methods)
for item in user.keys():
  print(item)
#Output:
# name
# age
# can_swim

print()

# Since you already know that .item() returns key-value pairs in tuples, you can unpack the tuples and display the keys and values separately
for key, value in user.items():
  print(key, value)
#Output:
# name Golem
# age 5006
# can_swim False