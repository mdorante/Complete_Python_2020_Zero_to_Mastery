my_list = [5, 4, 3]

# Write a lambda expression that prints out a squared version of my_list (all items to the power of two)
print(list(map(lambda item: item ** 2, my_list)))  # [25, 16, 9]

a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# Write a lambda expression that orders this list by the second item in the tuples
# Ex: [(10,-1), (0,2), (4,3), (9,9)]

# sort() iterates through each item of a list and then returns a sorted list
a.sort(key=lambda x: x[1])
# what we did here was tell sort the key by which it was going to iterate,
#  the lambda function takes an item and returns the index 1 of that item
print(a) # [(10, -1), (0, 2), (4, 3), (9, 9)]

