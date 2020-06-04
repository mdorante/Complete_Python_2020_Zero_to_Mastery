# super() -> keyword that refers to the superclass of the class it is used in
# it's useful when you want to call a method of a parent class from inside the subclass


class User:  # Parent Class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):  # subclass or derived class of User
    def __init__(self, name, power, email):
        # Here we're calling the email dynamic attribute from the __init__ method of the User class
        super().__init__(email)
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


wizard1 = Wizard('Merlin', 80, "merlin@gmail.com")

print(wizard1.email)  # merlin@gmail.com
