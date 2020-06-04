# Decorators allow us to supercharge a function, that is: add new functonalities to it without
# modifiying its original structure

# Higher Order Function (HOC): it can be 2 things
# 1 - A function that accepts another function as a parameter
# 2 - A function that returns another function

# NOTE: map(), filter() and reduce() are all HOC


# Let's say we have a function that prints Hello, we can create a decorator that can take that Hello
# function and add asterisks above and below the Hello

def my_decorator1(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello():
    print('Hello')


def bye():
    print('bye')


@my_decorator
def bye2():
    print('bye')


bye()
# Output:
# bye

bye2()
# Output:
# **********
# bye
# **********

hello()
# Output:
# **********
# Hello
# **********

# NOTE: The decorator takes a function as a parameter, modifies it and outputs the modified function

print()

# Decorators can also be used with functions that take parameters in


def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func


@my_decorator2
def greeting(name, emoji):
    print(f'Hey {name} {emoji}')


greeting('Manuel', 'xD')
# Output:
# **********
# Hey Manuel xD
# **********

# NOTE: This is the Python Decorator Pattern, it's widely used in Python to 'decorate' functions


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func
