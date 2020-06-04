from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap_this(item):
    return item.capitalize()


my_pets_caps = list(map(cap_this, my_pets))
print(my_pets_caps)  # ['Sisi', 'Bibi', 'Titi', 'Carla']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

ordered_zipped = list(zip(my_strings, sorted(my_numbers)))
print(ordered_zipped)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(item):
    return item > 50


filtered_scores = list(filter(over_50, scores))
print(filtered_scores)  # [73, 65, 76, 100, 88]

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores).
#  What is the total?


def total_sum(acc, item):
    return acc + item


total = reduce(total_sum, (my_numbers + scores), 0)
print(total)  # 456
