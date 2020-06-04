# We can use try and except for handling an error

# Let's say we're simply asking the user for their age
# If the user types in anything besides a number, we'll get a ValueError because the Python Interpreter
# can't turn that into an int
# Try means: try this code, but if it errors out, catch it with an exception
# this way, the whole program doesn't crash

while True:
    try:  # checks if this code works or if it errors out
        age = int(input('How old are you? '))
    except:  # it catches a possible error and does something about it
        print('Please enter a number')
    else:
        print(f'Your age is: {age}')
        break

# What if the program takes that age and divides 10 by that?
# We would have to add a specific exception for each specific error so we wouldn't have a buggy program
while True:
    try:
        age = int(input('How old are you? '))
        weird_var = 10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
    else:
        print(f'Your age is: {age}')
        break
