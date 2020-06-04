# Default Parameters and Keyword Arguments

# Default Parameters: Default values for parameters, specified during the Function Definition
def say_hello(name='Darth Vader', emoji='🤖'):
  print(f'Hello {name} {emoji}')

# If no arguments are specified, the Function will use the Default values
say_hello() # Hello Darth Vader 🤖

# If only one argument is specified, the others will remain with the defaults
say_hello('Naruto') # Hello Naruto 🤖

print()

#Positional Arguments
## The order in which we specify the arguments wil change the output
say_hello('Manuel', '🤓') # Hello Manuel 🤓
say_hello('🤓', 'Manuel') # Hello 🤓Manuel
#NOTE: Best practice, use this method but make sure to have your order right

print()

## Keyword Arguments: when we specify the arguments with the repective key-value pair, the position or order doesn't make a difference
say_hello(name='Eduardo', emoji='🤔') # Hello Eduardo 🤔
say_hello(emoji='🥰', name='Patricia') # Hello Patricia 🥰
#NOTE: This is a bad practice, it can be confusing for another developer to read