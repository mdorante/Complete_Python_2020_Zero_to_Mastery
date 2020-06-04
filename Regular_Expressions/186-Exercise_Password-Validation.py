# Use a regular expression to check if a password meets the following requirements
# At least 8 characters long
# Can contain any letter, number or any of these: $%#@
# has to end with a number

import re

pattern = re.compile(r"[a-zA-Z0-9@#$%]{7,}[0-9]$")

password1 = 'poi@k7#6%m8'
password2 = 'pakajdq8%$ani'
password3 = '9$a#lñ8'

a = pattern.fullmatch(password1)
b = pattern.fullmatch(password2)
c = pattern.fullmatch(password3)
print(a)  # <re.Match object; span=(0, 11), match='poi@k7#6%m8'>
print(b)  # None
print(c)  # None
