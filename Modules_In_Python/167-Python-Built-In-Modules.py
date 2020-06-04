import random

# returns a randon number between 0 and 1
print(random.random())
# Output:
# 0.21514754907917577

# returns a random integer from a given interval
print(random.randint(1, 10))
# Output:
# 4

# returns a random element from an iterable
print(random.choice([1, 3, 4, 'a', 3, 6, 'this']))
# Output:
# 6

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # shuffles the elements (in-place)
print(my_list)
# Output:
# [2, 4, 1, 3, 5]
