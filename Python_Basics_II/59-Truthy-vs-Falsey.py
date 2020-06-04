# Truthy and Falsey

# a Truthy value is one that when converted into a bool, evaluates to True
print(bool('hello')) # True
print(bool(5)) # True

# a Falsey value is one that when converted into a bool, evaluates to False
print(bool('')) # False
print(bool(0)) # False

username = 'coderdude'         
password = 'worstpasswordever' # these are Truthy values because they exist, Falsey values are usually empty objects or 0

if username and password:
  print('The user exists')
else:
  print('username or password invalid')

# All values are considered "truthy" except for the following, which are "falsy":

# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0