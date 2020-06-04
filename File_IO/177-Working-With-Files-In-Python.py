# There's a built in function in Python for file IO
# it's the open() function

# Let's say we have a text file in the same directory as this script, we can access it with open()

my_file = open('test.txt')

print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

print(my_file.read())
# Output:
# This is just a test
# I wanna check out if open() works the way I think it works

print()

# NOTE: You can only read the file once, using multiple my_file.read() statements will still only return
# the file contents once because it uses a cursor to read the file, and it doesn't automatically reset
# to the start of the file
print(my_file.read())  # no output
print(my_file.read())  # no output

print()

# But if we use the seek() method, which moves the cursor to whatever index we tell it to,
# we can then read the file again
my_file.seek(0)
print(my_file.read())
# Output:
# This is just a test
# I wanna check out if open() works the way I think it works

print()

my_file.seek(7)
print(my_file.read())
# Output:
#  just a test
# I wanna check out if open() works the way I think it works

print()
my_file.seek(0)
# We can read a file line by line by using the readline()

print(my_file.readline())  # This is just a test

print(my_file.readline())
# Output:
# I wanna check out if open() works the way I think it works

print()
my_file.seek(0)

# readlines() returns a list with all of the lines
print(my_file.readlines())
# Output:
# ['This is just a test\n', 'I wanna check out if open() works the way I think it works']

# NOTE: We have to manually close the file after we open it, so we can use the file somewhere
# else in the program
my_file.close()
