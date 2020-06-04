# We can also raise our own errors when we want the program to stop running before it crashes out

while True:
    try:
        age = int(input('What is your age?'))
        10/age
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        raise ZeroDivisionError('hey, cut it out')
    else:
        print('thank you')
    finally:
        print('ok, done here')

# If we run the program and input 0, we would get the following output:
# Traceback (most recent call last):
#   File "/home/manuel/gitProjects/python/Complete Python Developer 2020: Zero to Mastery/Advanced_Python_Error_Handling/155-Error-Handling-3.py", line 9, in <module>
#     raise ZeroDivisionError('hey, cut it out')
# ZeroDivisionError: hey, cut it out
