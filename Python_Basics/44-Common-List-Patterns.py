bag = ['a','b','c','z','u','b']

# Two ways I can sort this list
print(sorted(bag)) # returns a sorted copy of the list
print()
# OR
bag.sort() # sorts the list [in-place]
print(bag)
print()

# Two ways I can reverse the order of this list
print(bag[::-1]) # list slicing, just creates a copy of the list, reading it from end to start
print()
# OR
bag.reverse() # reverses the order of the list [in-place]
print(bag)
print()

# Generating a list quickly
print(list(range(100))) # creates a list with items ranging from numbers 0 to 99 (100 total)
print()

print(list(range(9,100))) # creates a list with items ranging from numbers 9 to 99 
print()

# .join() -> joins all the items in a list with the value of whatever string the method is working on
sentence = ' '
new_sentence = sentence.join(['Hi','my','name','is','Manuel'])
print(new_sentence)

new_sentence2 = ' '.join(['This','is','another','example'])
print(new_sentence2)