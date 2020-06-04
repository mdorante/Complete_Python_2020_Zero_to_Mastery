# Return

# Suppose we want to define a sum() function, (which already exists, but we want to create our own)
def sum(num1, num2):
  return num1 + num2  # we are telling the interpreter to exit the function with whatever the value of num1 + num2 is

print(sum(5, 4))  # 9
print(sum(1, 2))  # 3

print()

# Rule of thumb:
## A function should do one thing really well (can do multiple things but it's better to have a function for each thing for readability)
## A function should return something

total = sum(10,5)
print(sum(10,total)) # 25

print()

# We can define a function inside of another function

def plus(num1, num2):
  def plus2(n1, n2):   # Inside of the plus function, we define another function which actually sums two numbers
    return n1 + n2  # returns the sum
  return plus2(num1, num2) # we define what the plus funcion returns, which would be the result of giving the plus2 function, the parameters given to the plus function

total = plus(10, 20)
print(total) # 30

#NOTE: The return statement exits the function, if there are any lines of code after the return statement, they will never be executed