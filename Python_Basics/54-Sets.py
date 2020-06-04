# Sets: Un-ordered collections of unique objects

set1 = {1,2,3,4,5}
print(set1) # {1, 2, 3, 4, 5}

# duplicate items never get added, even though it may look like they were added, when you display the contents of the set, you will see no duplicates

set1 = {1,2,3,4,5,5,5,5,5}
print(set1) # {1, 2, 3, 4, 5}

print(len(set1)) # 5 (because the duplicates don't count)

# .add() -> adds an item (doesn't add if it's a duplicate)
set1.add(3) 
set1.add(100)
set1.add(2)
print(set1) # {1, 2, 3, 4, 5, 100}

# .set() -> turns an object into a set 
## suppose you have a list and you need to display it without duplicates

list1 = ['a','b','c','d','b']

print(set(list1)) # {'b', 'c', 'a', 'd'}  #it removes the duplicates, but doesn't maintain the order