# Let's say we have this function that takes a list and multiplies all it's items by 2


from functools import reduce


def mult_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(mult_by2([1, 2, 3]))  # [2, 4, 6]

# We can clean up the code by using Functional Programming
# We can use the map() function which takes a function, and applies it to a set of data

# map() takes the function and loops through all the items of the iterable, applying it to each one
# it returns a map object, which can be converted into a data set of it's own

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


new_list = list(map(multiply_by2, my_list))
print(new_list)  # [2, 4, 6]
print(my_list)  # [1, 2, 3]
# NOTE: There were no changes made to the original data set I used the function on
# That's because it's a pure function, one that doesn't affect the outside world and only modifies what
# goes into it

print()

# filter() takes a function and applies it to each item in a set of data, each iteration will return
# a truthy or falsey value, the truthy ones will be added to a new data set
# It's best used with functions that return a boolean

print(list(filter(multiply_by2, my_list)))  # [1, 2, 3]
# returns [1, 2, 3] because none of these values are Falsey


def only_odd(item):
    return item % 2 != 0


new_list2 = list(filter(only_odd, my_list))

print(new_list2)  # [1, 3]
# returns [1, 3] because these are the only items that return a truthy value

print()

# zip() takes two or more iterables and "zips" them together

list1 = [1, 2, 3, 4, 5]
tuple1 = (10, 20, 30)
list2 = [100, 200, 300, 400]

zipped_list = list(zip(list1, tuple1, list2))
print(zipped_list)  # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]
# NOTE: it groups each of the items with the same index into a tuple, and the length of the new data set
# will be the length of the shortest iterable

print()

# reduce() Apply a function of two arguments cumulatively to the items of a sequence
#  so as to reduce the sequence to a single value.


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# NOTE: the initial value for the acc value can be set as a third parameter for the reduce() function
accumulate = reduce(accumulator, list1, 0)
print(accumulate)
# Output:
# 0 1
# 1 2
# 3 3
# 6 4
# 10 5
# 15
