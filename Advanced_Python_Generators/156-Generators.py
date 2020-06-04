# A Python generator is a function that produces a sequence of results.
# It works by maintaining its local state, so that the function can resume again exactly where it left off
# when called subsequent times.
# Thus, you can think of a generator as something like a powerful iterator.

# It only keeps the recent data in memory

# Generators are really useful when calculating large sets of data because of it's optimized
# memory usage


def generator_function(num):
    for i in range(num):
        yield i + 1  # yield works like return
# This generator function creates a range of a given amount of numbers, one by one, not in a list


g = generator_function(5)
print(next(g))  # 1
print(next(g))  # 2
next(g)
next(g)
print(next(g))  # 5

# NOTE: If we try to use next() outside of the generator range, we will get a StopIteration error
print(next(g))
# Output:
# Original exception was:
# Traceback (most recent call last):
#   File "/home/manuel/gitProjects/python/Complete Python Developer 2020: Zero to Mastery/Advanced_Python_Generators/157-Genetartors-2.py", line 21, in <module>
#     print(next(g))
# StopIteration
