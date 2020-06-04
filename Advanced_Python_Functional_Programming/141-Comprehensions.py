# List, set, dictionary comprehensions: a quick way for us to create lists, sets or dictionaries
# without looping or appending stuff

# List Comprehension

my_list = [char for char in 'Akatsuki']
print(my_list)  # ['A', 'k', 'a', 't', 's', 'u', 'k', 'i']

my_list2 = [num for num in range(10)]
print(my_list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list3 = [num * 2 for num in range(10)]
print(my_list3)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_list4 = [num ** 2 for num in range(0, 11) if num % 2 == 0]
print(my_list4)  # [0, 4, 16, 36, 64, 100]

print()

# Set Comprehension: same as list comprehension but with sets

my_set = {char for char in 'Tsukuyomi'}
print(my_set)  # {'o', 'k', 'i', 'm', 'T', 's', 'y', 'u'}

my_set4 = {num ** 2 for num in range(0, 11) if num % 2 == 0}
print(my_set4)  # {0, 64, 4, 36, 100, 16}

print()

# Dictionary Comprehension

# Using an existing dictionary, we can create a new one with the data modified

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict = {k*2: v+2 for k, v in simple_dict.items()}
print(my_dict)  # {'aa': 3, 'bb': 4, 'cc': 5}

# Suppose we have a list and we want to create a dictionary where the keys are the items of the list
# and the values are the same items multiplied by 2

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)  # {1: 2, 2: 4, 3: 6}
