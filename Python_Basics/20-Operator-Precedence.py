#Operator Precedence

##Order 
#1 () 
#2 **
#3 * and /
#4 + and -

print((29 -4) + 2 ** 2) #29
print()

print((5 + 4) * 10 / 2) #45.0

print(((5 + 4) * 10) / 2) #45.0

print((5 + 4) * (10 / 2)) #45.0

print(5 + (4 * 10) / 2) #25.0

print(5 + 4 * 10 // 2) #25