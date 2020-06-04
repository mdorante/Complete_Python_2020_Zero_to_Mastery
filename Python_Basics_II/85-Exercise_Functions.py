# Create a function that takes a list of numbers and returns the biggest even number

def highest_even(li):
  '''
  This function returns the highest even number in a list
  '''
  highest = 0
  for item in li:
    if item % 2 == 0 and item > highest:
        highest = item
  return highest

print(highest_even([1,3,5,8,10,8,48,18,97])) # 48
print(highest_even([100,9,81,123,9287,234,23498,98,1,24])) # 23498

print()

# Andrei's solution
def highest_even2(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even2([1,9138,27,987,742,67])) # 9138
print(highest_even2([123,43,56,34,4,56,34,76,45,87])) # 76