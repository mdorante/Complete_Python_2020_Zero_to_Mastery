# More List Methods

list1 = ['a','z','b','c','d','e','d']

# .index() -> returns the index for the first appearance of an object
print(list1.index('d'))

# start and end for the search can also be specified
print(list1.index('c',0,4)) # starts search at index 0 and ends right before index 3

# .count() -> counts the ocurrences of an object
print(list1.count('d')) # 2

# .sort() -> organizes a list [in-place]
list1.sort()
print(list1) # ['a', 'b', 'c', 'd', 'd', 'e', 'z']

# sorted(list) -> returns an organized version of the list
print(sorted(list1)) # ['a', 'b', 'c', 'd', 'd', 'e', 'z']


# .copy() -> returns a copy of the list
list2 = list1.copy()
print(list2)

# .reverse() -> reverses the order of the list
list2.reverse()
print(list2)