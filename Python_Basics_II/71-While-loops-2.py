# While vs For

# For loops are better if you know how many times you will loop over an iterable
# While loops are better if you don't know how many times you will iterate

my_list = [1,2,3]

for item in my_list:
  print(item)
#Output:
# 1
# 2
# 3

print()

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
#Output:
# 1
# 2
# 3

# Good example for while
while True:
  response = input('say something: ')
  if response == 'bye':
    break
# In this case, it's impossible to know how many times the user will input something besides 'bye'