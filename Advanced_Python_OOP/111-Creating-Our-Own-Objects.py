# OOP

# Creating our own class and objects


class PlayerCharacter:
    def __init__(self, name):  # This is the constructor method or init method, it will be called everytime we instantiate an object
        self.name = name  # What we're saying is, when an object of this class is instantiated, take a parameter as name assign it to the name attribute

    def run(self):
        print(f'{self.name} is running!')
# NOTE: in classes, the first parameter for classes is always self, which refers to the actual class


player1 = PlayerCharacter('Manuel')
player2 = PlayerCharacter('Patricia')

print(player1.name)  # Manuel
print(player2.name)  # Patricia

player1.run()  # Manuel is running!
player2.run()  # Patricia is running!
