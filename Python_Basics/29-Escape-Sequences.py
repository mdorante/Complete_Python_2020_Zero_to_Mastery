# Escape Sequences

weather = "It's sunny" #Single quotes can be enclosed by double quotes
print(weather) #It's sunny
print()

weather = 'this is "kinda" cool" ' #Double quotes can be enclosed by single quotes
print(weather) #this is "kinda" cool
print()

weather = 'It\'s "kinda" hot' # backslash \ treats what ever comes after it as a string
print(weather) #It's "kinda" hot
print()

weather = "It\'s \"kinda\" cold"
print(weather) #It's "kinda" cold
print()

#\t -> tab
#\n -> new line

last_one = "\t Look at this tab! \n and look at this new line"
print(last_one)