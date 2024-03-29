# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 7)
cat2 = Cat('Carl', 20)
cat3 = Cat('Richard', 6)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    oldest = 0
    for cat in args:
        if cat.age > oldest:
            oldest = cat.age
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'The oldest cat is ')
oldest_cat_age = oldest_cat(cat1, cat2, cat3)
print(f'The oldest cat is {oldest_cat_age} years old')

print()

# Andrei's solution
# Note that the code is cleaner

# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
