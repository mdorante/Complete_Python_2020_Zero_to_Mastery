# The sys module is a really popular one because of functions like argv that can interact
# with a terminal

# For example, let's write a script that says hi to a user and takes the users name and last name
# as arguments from terminal input

import sys

name = sys.argv[1]
last_name = sys.argv[2]

print(f'Hi {name} {last_name}')

# If we enter the following into a terminal in the same directory where the python file is:
# python3 168-Python-Built-In-Modules-2.py Manuel Dorante

# We would get the following output: Hi Manuel Dorante
