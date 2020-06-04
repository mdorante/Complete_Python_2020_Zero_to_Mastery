# Conditional Logic

is_old = False
is_licensed = True

# If condition

if is_old and is_licensed: # if the condition evaluates to True, the code block below will execute 
  print('You can drive!') # the code block is defined by indentation, any lines of code that are indented are part of this "if" code block
else: # if both the above conditions evaluate to False, this is the code block that will be executed
  print('You can\'t drive')
print('whateverwhatever') # This line is not a part of the "if" code blocks, it will be executed no matter what the conditions of the "if" evaluate to

# elif can be used to add more conditions to the logic