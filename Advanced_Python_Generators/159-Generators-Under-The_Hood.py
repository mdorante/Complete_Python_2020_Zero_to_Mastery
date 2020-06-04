# Let's create our own for loop


def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


my_for([1, 2, 3])
# Output:
# 1
# 2
# 3

print()

# What about our own range() function, can we create that?


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


my_range = MyGen(0, 5)
for i in my_range:
    print(i)
#Output:
# 0
# 1
# 2
# 3
# 4
