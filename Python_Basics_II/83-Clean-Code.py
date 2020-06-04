# Clean Code

# Let's say we have this function that checks if a number is even

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

print(is_even(10)) # True
print(is_even(7))  #False

print()

## We can clean up the code by removing redundancies, like this
def is_even2(num):
  return num % 2 == 0  # num % 2 == 0 will return True or False

print(is_even2(9)) # False
print(is_even2(38)) # True

# This is possible because we know that expressions like (num % 2 == 0) will return a Truthy or Falsey value, so it's redundant to use an if statement with a return for each case because the expression by itself will already return True or False