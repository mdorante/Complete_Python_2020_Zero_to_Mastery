import utility  # imports all usable contents from this file

from shopping.more_shopping.shopping_cart import buy  # imports a function from a module

# we can also import the whole file, it would look something like this:
# from shopping.more_shopping import shopping_cart

print(buy('apple'))  # ['apple']

print(utility.divide(10, 5))  # 2.0
print(utility.multiply(3, 9))  # 27

# NOTE: When we import functions from a module, we can just directly use them (line 8),
# when we import a whole module, we need to call the module every time we want to
# call a function from that module (lines 10-11)

# __name__ returns the name of the current file
# Ex: a print(__name__) statement in shopping_cart.py would return shopping.more_shopping.shopping_cart
# whenever we are on the main file, no matter what the actual name of the file is, __name__ will
# return __main__ for this file

if __name__ == '__main__':
    print('please run this')

# Importing a useless package like in lesson 171-pip-install,
# this was downloaded from file->settings->project interpreter-> '+' button
import pyjokes

print(pyjokes.get_joke('en', 'neutral'))
# Output:
# A product manager walks into a bar, asks for drink. Bartender says no, but will consider adding later.
