# Instance Methods: Can access unique data of ther instance, must have self as a parameter but you don't need to pass this in every time

# Static Methods: are related to a class in some way, but don’t need to access any class-specific data

# Class Methods: They can’t access specific instance data, but they can call other static methods.
# They don't need self but they do need cls, which is similar and stands for class


class Ninja:
    human = True  # Class Object Attribute

    def __init__(self, name, age):
        self.name = name  # dynamic attribute
        self.age = age  # dynamic attribute

    def say_hi(self):  # Instance Method
        print(f'Hi, my name is {self.name}')

    @classmethod  # Class Method
    def adding_things(cls, num1, num2):
        return num1 + num2

    # You can instantiate an object through a class method too
    @classmethod
    def subtracting_things(cls, num3, num4):
        return cls('Itachi', num3 - num4)

    @staticmethod  # Static Method
    def multiplying_things(n1, n2):
        return n1 * n2


print(Ninja.adding_things(1, 3))  # 4

ninja1 = Ninja.subtracting_things(24, 4)
print(ninja1.name)  # Itachi
print(ninja1.age)  # 20
ninja1.say_hi()  # Hi, my name is Itachi
