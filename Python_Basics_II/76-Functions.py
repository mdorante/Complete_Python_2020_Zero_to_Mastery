# Functions

# def -> tells the interpreter we're about to define a function

##parameters -> dynamic variables that I can use inside of functions
### Parameters are used when we DEFINE the function
def say_hello(name, emoji):   # name and emoji are parameters
  print(f'Hello {name} {emoji}')

##arguments -> values we provide to the function's parameters (dynamic variables)
### Arguments are used when we CALL the function
say_hello('Manuel', '🤓') # 'Manuel' and '🤓' are arguments
#Output:
# Hello Manuel 🤓

say_hello('Andrei', '🤣') # Hello Andrei🤣
say_hello('Dan', '💀') # Hello Dan💀