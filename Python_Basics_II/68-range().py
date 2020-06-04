# range() -> returns an object that produces a sequence of integer from start (inclusive) to stop (exclusive)

for number in range(100):
  print(number)     # prints numbers 0 to 99, each on a new line

print()

# you can also specify where to start the range
for number in range(9,110):
  print(number) # prints numbers from 9 to 109

print()

# you can do things repeatedly in a loop without ever using the iteration variable
## let's say you need to print 'Hey' 6 times
for item in range(6):
  print('Hey') 
#Output:
# Hey
# Hey
# Hey
# Hey
# Hey
# Hey

print()

### knowing that you don't need the iteration variable, you can just name it _
for _ in range(3):
  print('Kamehameha')
#Output:
# Kamehameha
# Kamehameha
# Kamehameha

for _ in range(3):
  print(_)
#Output:
# 0
# 1
# 2

print()

### stepover can also be specified for the range
for _ in range(0,10,2):
  print(_)
#Output:
# 0
# 2
# 4
# 6
# 8

print()

## if you need to iterate in reverse, you need to reverse the order of the range variables and use a negative stepover
for _ in range(5,0,-1):
  print(_)
#Output:
# 5
# 4
# 3
# 2
# 1

print()

### if you need to quickly create a list with n items, do a list(range(n))
my_list = list(range(5))
my_list2 = list(range(5,0,-1))
print(my_list) # [0, 1, 2, 3, 4]
print(my_list2) # [5, 4, 3, 2, 1]