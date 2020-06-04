# While loops

i = 0
while i < 10:
  print(i)
  i += 1
#Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print()

i = 0
while i < 10:
  print(i)
  i += 1
  break   # breaks out of the loop
#Output:
# 0

print()

i = 0
while i < 10:
  print(i)
  i += 1
else:  #This code block will only execute when the while statement evaluates to False
  print('Done with the loop')