# Best Practice: Always catch errors based on specific exceptions


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # we can get a more concise description of the error by doing something like this
        print(f'Please enter numbers, {err}')


print(sum('1', 3))
# Output:
# Please enter numbers, can only concatenate str (not "int") to str

print()

# We can also group exceptions together
# And theres a 'finally' statement that can be used and it will execute regardless of the try-except blocks


def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    finally:
        print('This will be printed anyway')

# print(div(1,0))
# Output:
# division by zero


print(div(1, 'z'))
# Output:
# unsupported operand type(s) for /: 'int' and 'str'
# This will be printed anyway
