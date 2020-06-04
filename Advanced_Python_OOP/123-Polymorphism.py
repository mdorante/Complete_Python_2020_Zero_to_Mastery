# Polymorphism: object classes can share the same method names, and these methods can act differently
# based on the object that calls them

# Polymorphism is the ability to re-define methods


class User:  # Parent Class
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):  # subclass or derived class of User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # I'm calling the User class version of attack from inside the Wizard class
        print(f'Attacking with the power of {self.power}')


class Archer(User):  # subclass or derived class of User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Harry', 'Avada Kedabra')
archer1 = Archer('Robin Hood', 187)

# Polymorphism Example:


def player_attack(char):
    char.attack()


player_attack(wizard1)
# Output:
# do nothing
# Attacking with the power of Avada Kedabra

print()

player_attack(archer1)  # Attacking with arrows: arrows left- 187

# Note how the same function does a different thing when called upon by different objects
