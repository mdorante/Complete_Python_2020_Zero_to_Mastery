# For loops

for item in 'iterable':
  print(item)
print()

#iterable is any object that can be looped through (lists, strings, sets, etc.)
#item is a variable used to loop through the iterable, it can have any name

for dude in 'iterable':
  print(dude)
print()

# loops can be nested inside other loops as well

for number in (1,2,3,4,5):
  for letter in ['a','b','c']:
    print(number, letter)
  print()