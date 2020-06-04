# MRO is a rule that defines the order in which an object will try to call a method

# mro() -> function that returns the order in which an object will resolve a method call


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())
# Output:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

print(D.num) # 1

# When calling a method from D, it will look for the method in the scope of D
# if it's not found, it will look in class B, then in class C, then in class A
# and the last try will be in class object, only if it's not found even in this scope, the interpreter will error out

# MRO for D
#    A
#   / \
#  /   \
# B     C
#  \   /
#   \ /
#    D
