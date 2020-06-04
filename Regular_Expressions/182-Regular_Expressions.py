# In order to use RegEx, we have to import the re library

import re

# Suppose we have a string and we want to search for a substring inside of it

str1 = 'Hi what\'s up, I just wanna check this out to search this real quick'

# We can do a normal search, that will return a True or False
print('just' in str1)  # True

print()

# But we can do more by using RegEx

print(re.search('just', str1))  # returns a match object
# Output:
# <re.Match object; span=(16, 20), match='just'>
# the span tells us where the pattern begins in the string and where it ends

print()

# Let's see what else we can do with the match object
a = re.search('just', str1)
print(a.span())  # (16, 20)
print(a.start())  # 16
print(a.end())  # 20

print()

# If we search for a pattern that isn't in the string, it will return a None object and will error out
# if we try to print it

# We can also use the compile() method to create a pattern object
pattern = re.compile('this')

b = pattern.findall(str1)
c = pattern.fullmatch(str1)
print(b)  # ['this', 'this']
print(c)  # None
# NOTE: fullmatch() will return a match object if the pattern is actually the same exact thing as the string

print()

# Let's use regex to find a pattern in the string

# This pattern searches for a match that starts with any letter, then has any character and then an 'a'
pattern2 = re.compile(r"([a-zA-Z]).([a])")

m = pattern2.search(str1)
print(m.group())  # wha
print(m.group(1))  # w
print(m.group(2))  # a
