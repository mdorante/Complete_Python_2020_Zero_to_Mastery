# Docstrings: Documentation for your custom defined functions, they should contain useful info for other devs or even for your future self about what the function does and how it works

def test(a):
  '''
  Info: this is the docstring
  info2: this function tests and prints param a
  '''
  print(a)

test(9) # 9

print()

# If you don't know what a function does, you can find out with the help() function
help(test)
#Output:
# Help on function test in module __main__:

# test(a)
#     Info: this is the docstring
#     info2: this function tests and prints param a

print()

# If you want to print out the docstring for a function, you can use the __doc__ method
print(test.__doc__)
#Output:

  # Info: this is the docstring
  # info2: this function tests and prints param a