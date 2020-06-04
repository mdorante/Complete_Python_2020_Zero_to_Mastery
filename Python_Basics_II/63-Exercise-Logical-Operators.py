# We're creating a character for a game

is_magician = False
is_expert = True

# If you're a magician and an expert, "you are a master magician"
# If you're a magician but not an expert, "at least you're getting there"
# If you're not a magician, "you need magic powers"

if is_magician and is_expert:
  print('You are a master magician')
elif is_magician and not is_expert:
  print('At least you\'re getting there')
elif not is_magician:
  print('You need magic powers')