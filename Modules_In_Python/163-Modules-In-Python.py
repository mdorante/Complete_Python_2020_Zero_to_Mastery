# Modules are Python files, you can have them interact with each other and organize your projects this way
# In this example we created a utility file in the same directory where we have this file,
# and we imort the file and use som functions that were defined in that file
import utility

print(utility)
# Output:
# <module 'utility' from '/home/manuel/gitProjects/python/Complete_Python_Developer_2020/Modules_In_Python/utility.py'>

print(utility.divide(10, 5))  # 2.0
print(utility.multiply(2, 3))  # 6

# A Package is a Directory that contains Modules
# Check out the modules directory, that's the folder where we created the PyCharm project for these lessons

# When we import a file, the interpreter runs that file and keeps all the usable content in memory (cache) in order to use them
# Any statements that are written on the modules we import, will be executed when we run the program
# Ex: if we have a print('hi') statement in the dudes.py module and we import it at the beginning of the main file,
# when we run the program, the first thing that will outut to the screen will be hi
