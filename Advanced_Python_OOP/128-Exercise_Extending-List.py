# Create a class Superlist that creates objects with all the attributes and methods that lists have
#  and the len() should return 1000 no matter how many items the list has


class Superlist(list):

    def __len__(self):
        return 1000


super_list1 = Superlist()

print(len(super_list1))  # 1000

super_list1.append(5)
print(super_list1[0]) # 5

print(isinstance(super_list1, list)) # True