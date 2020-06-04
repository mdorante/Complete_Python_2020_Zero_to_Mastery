# Dunder methods are special methods that allow us to use Python specific functions on our objects or classes

# dir() -> returns all the methods (including dunders) and attributes accessible by an object
# if no object is given, it will return the methods and attributes accessible in the current scope


class Toy:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):  # Dunders can be modifed to do different things for different classes
        return f'{self.color}'

    def __len__(self):
        return 3000000


action_figure = Toy('red', 'Small')
num = [1, 2, 3, 4, 5, 6, 7]

# Using .__str__() does exactly the same as using str(), because __str__ is a method that enables the str() function
# Remember that str() converts an object into a string
print(action_figure.__str__())  # red
print(str(action_figure))  # red
# Note how the str() function is actually returning the object's color,
# because we modified the dunder __str__ for
# the Toy class


# But when we use it on an object that is not a part of the class where we modified it, it has its default behavior
print(str(num))  # [1, 2, 3, 4, 5, 6, 7]
print(num.__str__())  # [1, 2, 3, 4, 5, 6, 7]

# The same goes for the __len__ dunder that was modified
print(len(action_figure))  # 3000000
print(len(num))  # 7
