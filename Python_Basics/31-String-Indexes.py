# String Indexes

eye = 'Sharingan'
#      012345678

print(eye[0]) #S
print(eye[6]) #g
print(eye[1]) #h

print()

# Subtstrings
# [start:stop:stepover]

print(eye[0:5]) #Shari
print()
print(eye[0:8]) #Sharinga
print()
print(eye[1:9]) #haringan
print()
print(eye[0:]) #Sharingan
print()
print(eye[:6]) #Sharin
print()
print(eye[0:9:1]) #Sharingan
print()
print(eye[1:]) #haringan
print()
print(eye[::1]) #Sharingan
print()
print(eye[1::2]) #hrna
print()
# Reverse index
print(eye[-1]) #n
print()
print(eye[-5]) #i
print()
print(eye[::-1]) #nagnirahS (reverses the string)
print()
print(eye[::-2]) #ngiaS