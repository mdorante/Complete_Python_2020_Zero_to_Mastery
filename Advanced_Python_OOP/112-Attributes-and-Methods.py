# OOP

#Attributes and Methods


class PlayerCharacter:

    # Class Object Attribute: an attribute that will be the same for every object of the class
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # dynamic attribute: different for every object
            self.age = age  # dynamic attribute

    def run(self):
        print(f'{self.name} is running!')

    def say_hi(self):
        print(f'Hi, my name is {self.name}')

# NOTE: Inside the class definition, you can access Class Object Atrributes by referring to the class itself
#  but for dynamic attributes, you must refer to the object(self) in order to access them


player1 = PlayerCharacter('Manuel', 23)
player2 = PlayerCharacter('Naruto', 16)

print(player1.age)  # 23
print(player2.age)  # 16

print(player1.membership)  # True
print(player2.membership)  # True

player1.run()  # Manuel is running!

# Using help(object) will display the blueprint for the object in question

# help(player1)
# Output:
# Help on PlayerCharacter in module __main__ object:

# class PlayerCharacter(builtins.object)
#  |  PlayerCharacter(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  run(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
