# the "nonlocal" keyword is used to tell the interpreter that you want to use a variable that isn't a global variable, but isn't in the scope of your function

def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner:", x)
  
  inner()
  print("outer:", x)

outer()
#Output:
# inner: nonlocal
# outer: nonlocal

#NOTE: when we used nonlocal x in line 8, we said that we wanted to use the x variable created in line 6. When it's modified in line 9, it's not a local modification, it actually modifies the variable at line 6