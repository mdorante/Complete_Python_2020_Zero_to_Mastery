# If you don't want to be careful about opening and closing files, there's another way to do it

# NOTE: This is the proper way to work with files in Python
with open('test.txt') as my_file:
    print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

# open() has a parameter that can be passed in for the mode in which we want to open the file
# by default it's set to 'r' for read, but we can use 'w' for writing to files or 'r+' for both
# read and write access

with open('test.txt', mode='r+') as my_file2:
    text = my_file2.write('Hey it\'s me!')
    print(text)  # 12 ## the amount of characters written to the file
    # If we check out the file, we will see that the text overwrote the first 12 characters in the file

# If we don't want to overwrite, we can use the append mode 'a' so that anything we write gets
# appended to the end of the file

with open('test.txt', mode='a') as my_file3:
    text2 = my_file3.write('xD')
    print(text2)  # 2 ## number of characters appended


# NOTE: The write() method does different things depending on the open() mode
# in 'r+' mode: it overwrites characters starting at index 0
# in 'w' mode: it overwrites the entire file
# in 'a' mode: it appends to the end of the file

# In 'w' mode, we can create a file that doesn't existe
with open('sad.txt', mode='w') as sad_file:
    text_sad = sad_file.write(':(')
    print(text_sad)  # 2

# NOTE: Absolute and relative paths can be used if we need to read or write files that
# aren't in the same directory as the python file we're trying to access from

# There's also a library called pathlib that will take care of file paths for you if
# you have a program that runs on windows as well as unix systems
