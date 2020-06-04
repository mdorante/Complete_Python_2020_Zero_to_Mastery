# List unpacking

# A list can be separated or unpacked into variables

basket = [1, 2, 3, 4, 5]
print(basket)  # [1, 2, 3, 4, 5]

#If I wanted to separate each value into a variable, I could just do this
a, b, c, d, e = [1, 2, 3, 4, 5]
print(a)  #1
print(b)  #2
print(c)  #3
print(d)  #4
print(e)  #5

# There's a few other cool things I can do, for example using RegEx

a, b, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(other)  # [3, 4, 5, 6, 7, 8, 9]

a, b, c,*middle,d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(middle)  # [4, 5, 6, 7, 8, 9, 10]
print(d) # 11
