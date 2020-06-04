# *args and **kwargs

#*args tells the Python interpreter that the function can receive any amount of arguments
#**kwargs tells the Python interpreter that the function can receive any amount of keyword arguments
def super_func(*args, **kwargs):
  print(*args)
  print(args) 
  print(kwargs)
  return sum(args) 

#NOTE: the sum() function is a default Python function that returns the sum of all of the parameters given to it

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))
#Output:
# 1 2 3 4 5
# (1, 2, 3, 4, 5)
# {'num1': 5, 'num2': 10}
# 15 

print()

# Example
def total_sum(*args, **kwargs):
  '''
  This function sums all the arguments and then sums that to the sum of all the values for the keyword arguments
  '''
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(total_sum(1,2,3,4,5, num1=5, num2=10)) # 30

# Rule for argument ordering: 
# Specify them in this order: params, *args, default params, **kwargs