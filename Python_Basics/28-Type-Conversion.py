# Type Conversion
a = 100
b = str(a) #str() converts an object into a string
c = int(b) #int() converts an object into an int
d = type(c)
print(d)   # <class 'int'>

print()

#This is the same thing in just one line
print(type(int(str(100)))) # <class 'int'>