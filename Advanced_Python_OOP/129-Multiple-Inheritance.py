# Let's say we have a class with two subclasses
class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')

    def heal(self):
        print(f'100% healed')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} arrows remaining')

    def attack(self):
        print('wejo')

# If we want to create a class that is a subclass of Wizard and Archer


class HybridDude(Wizard, Archer):
    def __init__(self, name, power, arrows):
        # This calls the Archer constructor and passes name and arrows to it
        Archer.__init__(self, name, arrows)
        # This calls the Wizard constructor and passes name and power to it
        Wizard.__init__(self, name, power)


hd1 = HybridDude('Bob', 'lightning', 99)

hd1.attack()  # attacking with the power of lightning
hd1.check_arrows()  # 99 arrows remaining
