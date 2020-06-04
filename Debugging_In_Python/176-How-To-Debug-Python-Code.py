# We can debug our python code using the Python DeBugger (pdb)

# Just import it in the file you want to debug and write a pdb.set_trace() where you
# want to start debugging

# It's an interactive interface with a lot of options (help will display all available commands)
# Some of the commands are:
# a - list all the arguments for the current function
# s -  run the code line by line
# l - list the source code for the current file

import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 'asd')
