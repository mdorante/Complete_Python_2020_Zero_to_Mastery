# enumerate() -> returns index values in tuples for an iterable object

for char in enumerate('Hello!'):
  print(char)
#Output:
# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
# (5, '!')

print()

## iterables can be unpacked in the loop statement
for i, char in enumerate('Dude'):
  print(i, char)
#Output:
# 0 D
# 1 u
# 2 d
# 3 e

print()

# enumerate a list of numbers 1-10 and display the index for number 5
for i, char in enumerate(list(range(1,11))):
  if char == 5:
    print(f'The index for {char} is {i}')
#Output:
# The index for 5 is 4