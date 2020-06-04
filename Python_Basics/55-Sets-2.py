# More Set Methods

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# set1.difference(set2) -> returns the items in set1 that aren't in set2
print(my_set.difference(your_set)) # {1, 2, 3}
print(your_set.difference(my_set)) # {6, 7, 8, 9, 10}

# .discard() -> removes an item from a set if it exists
my_set.discard(3) 
print(my_set) # {1, 2, 4, 5}

# .difference_update() -> removes all elements from another set that exist in this set
my_set.difference_update(your_set)
print(my_set) # {1, 2} ##4 and 5 were removed

### Let's reset the sets
print()
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .intersection() -> returns the elements that exist in both sets
print(my_set.intersection(your_set)) # {4, 5}

# can also be done with a '&'
print(my_set & your_set) # {4, 5}

# .isdisjoint() -> returns True if the sets have no common elements
print(my_set.isdisjoint(your_set)) # False

# .union() -> returns a set that unites both sets while removing duplicates
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# can also be done with a '|'
print(my_set | your_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print()

our_set = my_set.union(your_set)

# set1.issubset(set2) -> returns True if set2 contains set1
print(my_set.issubset(our_set)) # True

# set1.issuperset(set2) -> returns True if set1 contains set2
print(our_set.issuperset(your_set)) # True