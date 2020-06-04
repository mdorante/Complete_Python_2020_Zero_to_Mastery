# List methods

basket = [1,2,3,4,5]

# Adding methods

# .append() -> appends an object to the end of a list, this happens [in-place]
# what this means is that it modifies the actual value of the object, it doens't produce output or create a copy of the object, it just goes and modifies the original object

print(basket.append(98)) # None, because there's no output for this operation, it just went and appended 98 at the end of the original list
print(basket) # [1, 2, 3, 4, 5, 98] see, the list is modified

# .insert() -> inserts an object at a specified list index [in-place]
basket.insert(0, 'a') 
print(basket) # ['a', 1, 2, 3, 4, 5, 98]

# .extend() -> extends a list with an iterable (list) [in-place]
basket.extend([100])
basket.extend([101,102])
print(basket)

print()

# Removing methods

# .pop() -> removes the item in the specified index (if no index is specified, it removes the last item by default) [non-in-place]
basket.pop() # removes last item
print(basket) 

basket.pop(0) # removes first item
print(basket)

#NOTE: .pop() returns the value that was removed as output
print(basket.pop()) # returns 101, which was the last value in the list, the one that got removed

# .remove() -> removes first ocurrence of a value [in-place]
basket.remove(100)
print(basket)

# .clear() -> removes all items from the list [in-place]
basket.clear()
print(basket) # []