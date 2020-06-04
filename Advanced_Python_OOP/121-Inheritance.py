# Classes can INHERIT attributes and methods from other classes


class User:  # Parent Class
    def sign_in(self):
        print('logged in')


class Wizard(User):  # subclass or derived class of User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with the power of {self.power}')


class Archer(User):  # subclass or derived class of User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 'fire')
archer1 = Archer('Hawkeye', 78)

wizard1.sign_in()  # logged in
archer1.sign_in()  # logged in

wizard1.attack()  # Attacking with the power of fire
archer1.attack()  # Attacking with arrows: arrows left- 78

print()

# isinstance() is a built in Python function that checks if an object is of a certain class
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True because Wizard is a subclass of User

print(isinstance(archer1, Archer))  # True
print(isinstance(archer1, Wizard))  # False
print(isinstance(archer1, User))  # True

print()

print(isinstance(archer1, object))  # True
# NOTE: All classes are a subclass of the python 'object' class and inherit all of its methods
