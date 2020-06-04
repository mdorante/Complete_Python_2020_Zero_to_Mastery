# Let's create an email checker
# We can just google the regex for checking an email

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

email = 'mdorante10@gmail.com'
email2 = 'Manuel'

valid = pattern.search(email)
valid2 = pattern.search(email2)

print(valid)  # <re.Match object; span=(0, 20), match='mdorante10@gmail.com'>
print(valid2)  # None
