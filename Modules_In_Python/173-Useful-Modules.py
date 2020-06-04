from array import array
import datetime
from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
word = 'kamehameha'

# Counter() creates an object that counts how many times an item appears in a container
print(Counter(li))
print(Counter(word))
# Output:
# Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# Counter({'a': 3, 'm': 2, 'e': 2, 'h': 2, 'k': 1})

print()

# defaultdict() returns a default value when trying to access a non-existent dictionary key
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['d'])  # does not exist

print()

# OrderedDict retains the order that you insert inside of a dictionary

dict1 = {'a': 100}
dict1['b'] = 1
dict1['c'] = 2

dict2 = {'c': 2}
dict2['a'] = 100
dict2['b'] = 1

print(dict1 == dict2)  # True

print()

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)  # False


# datetime.time() is used to create a time object with whatevr time you want
print(datetime.time())  # 00:00:00
print(datetime.time(5, 45, 17))  # 05:45:17

print()

# datetime.date.today() returns today's date
print(datetime.date.today())  # 2019-12-02

print()

# array can be used to create an array, which is basically an optimized list
# it's more performant than a list and less complicated than a generator

arr = array('i', [1, 2, 3])
print(arr)  # array('i', [1, 2, 3])
print(arr[0])  # 1
print(arr[1])  # 2
