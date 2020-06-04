# continue -> jumps back to the top of the loop

my_list = [1,2,3]

for item in my_list:
  continue
  print(item)

i = 0
while i < len(my_list):
  i += 1
  continue
  print(my_list[i])

## In both of these cases, nothing will be printed to the console because the "continue" statement makes the interpreter jump back to the top of the loop each time it gets hit until the loop ends, so basically, the intepreter never reaches lines 9 and 15

# pass -> just a line of code that can be executed but does nothing, works great as a place holder

### use case for pass
tuple1 = (1,2,3,4,5)
for number in tuple1:
  #Thinking about it, not sure what I need here yet
  pass

i = 0
while i < len(tuple1):
  print(tuple1[i])
  i += 1