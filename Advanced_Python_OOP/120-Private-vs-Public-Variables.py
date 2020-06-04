
class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running!')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')


character1 = Character('Manuel', 23)

# Since the name and speak variables aren't private, they can be modified at any time
character1.name = '!!!'
character1.speak = 'whatever'

# The Python convention for private variables is for the names to start with an _underscore
# it doesn't actually make them private because that can't be done in Python, so the best practice is to use
# an underscore so that any other dev that reads your code knows that those variables should not be touched

class PrivateCharacter:
    def __init__(self, name, age):
        self._name = name # "private" variables
        self._age = age

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')

