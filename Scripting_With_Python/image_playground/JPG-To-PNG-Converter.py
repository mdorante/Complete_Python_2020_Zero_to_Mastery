# Write a script that converts all the .jpg images in a directory to .png and stores them
# in a new directory

import sys
import os
from PIL import Image

# Grab first and second argument
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# Check if second argument (new folder) exists, if not, create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through pokedex, convert images to png and save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}/{clean_name}.png', 'png')
print('Files converted successfully')
