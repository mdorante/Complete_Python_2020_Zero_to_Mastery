# Built-in functions

# str()   -> converts an object into a string
# int()   -> converts an object into an integer
# type()  -> returns an objects type (int, float, str, etc.)
# print() -> prints values to the console
# len() -> returns the number of items in a container (characters in a string, objects in a list, etc.)


# String methods
# Usually start with a . (.format, .upper)

quote = 'to be or not to be'

# .upper() -> returns an all uppercase version of the string
print(quote.upper()) 

# .capitalize() -> returns a capitalized version of the string (makes first character uppercase and the rest lowercase)
print(quote.capitalize())

# .find() -> returns the index where a substring starts
print(quote.find('not')) 

# .replace() -> replaces all ocurrences of a substring (amount of ocurrences may be specified)
print(quote.replace('be', 'you'))

#NOTE: the versioned strings don't actually modify the original string
print(quote)

# What I can do is save the versioned string to another variable
quote2 = quote.replace('be', 'me')
print(quote2)