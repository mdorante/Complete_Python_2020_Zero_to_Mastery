# Dictionary keys can be any data type, except a list
## because dictionary keys must be immutable

dict1 = {
  986: [1,2,3],
  False: 'Amaterasu',
  'name': 'Manuel' # Usually a key is something descriptive
}

# A key must be uniqe, if the same key is used several times in the dictionary, each new appearance will overwrite the last

dict2 = {
  123: [1,2,3],
  True: 'Manu kicks ass',
  123: 'numbers'
}

print(dict2[123]) # numbers