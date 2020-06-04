# Exercise!
## Display this picture in the console, loop over the list and display a " " for every 0 and a * for every 1 in the items

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for line in picture:
  for i,item in enumerate(line):
    if (item == 0):
      line[i] = ' '
    elif (item == 1):
      line[i] = '*'
  print(''.join(line))
#Output:
#    *
#   ***
#  *****
# *******
#    *
#    *