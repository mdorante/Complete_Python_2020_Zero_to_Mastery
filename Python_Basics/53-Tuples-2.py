# Tuples can be sliced like lists (well, kinda)

my_tuple = (1,2,3,4,5,2)

# [start:end+1]
print(my_tuple[:]) # (1, 2, 3, 4, 5)
print(my_tuple[0:3]) # (1, 2, 3)

print(my_tuple[1:4]) # (2, 3, 4)

# .count() -> counts the appearances of a value
print(my_tuple.count(2)) # 2
print(my_tuple.count(4)) # 1

# .index() -> returns the index of the first appearance of a value
print(my_tuple.index(3)) # 2
print(my_tuple.index(2)) # 1