# List Slicing

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]

# Lists are mutable, items may be changed
amazon_cart[0] = 'laptop' #changed index 0 (notebooks) to laptops

# Copying lists

new_cart = amazon_cart # Here, new_cart is just a pointer that points to amazon_cart's value

new_cart[1] = 'ps4' # This doesn't only change the value on new_cart[0], it actually changes the value on amazon_cart[0] because new_cart[0] just points to that value

print(new_cart)    # ['laptop', 'ps4', 'toys', 'grapes']
print(amazon_cart) # ['laptop', 'ps4', 'toys', 'grapes']
print()

# If I want to copy the contents of a list, I could do the following
new_cart2 = new_cart[:]

# Now, if I modify new_cart2, new_cart won't be modified along with it
new_cart2[2] = 'Jordans'

# Check it out
print(new_cart2) # ['laptop', 'ps4', 'Jordans', 'grapes']
print(new_cart)  # ['laptop', 'ps4', 'toys', 'grapes']