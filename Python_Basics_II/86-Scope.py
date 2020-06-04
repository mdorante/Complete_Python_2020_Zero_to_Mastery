# Scope: The variables you have access to

# Function scope: any variables created inside of functions can only be accessed by that function

# Scope Rules for variables: where to look first
# 1 - Start with local scope (anything inside the current scope)
# 2 - Parent local scope (is the variable defined in a scope that encloses this scope?)
# 3 - Global (anything not enclosed by a function)
# 4 - If it's not in local, parent or global scope, then it must be a Python built-in function

a = 1

def parent():
  a = 5   #NOTE: This a is not the same a as the one in line 7! Because this one is inside the scope of confusion()
  def confusion():
    return a
  return confusion()

print(a) # 1
print(parent()) # 5