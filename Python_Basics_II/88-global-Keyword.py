# The "global" Keyword

# If you want to use a global variable inside a local scope
total = 0

def count():
  global total # this tells the interpreter to use the global "total" variable, created in line 6
  total += 1 
  return total

count()
count()
print(count()) # 3