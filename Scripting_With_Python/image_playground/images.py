from PIL import Image, ImageFilter

# creates an image object containing the .jpg file
img = Image.open('./Pokedex/pikachu.jpg')

print(img)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x7F7FCC41CAC0>
print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB


# Let's add a filter to the pikachu image
filtered_img = img.filter(ImageFilter.BLUR)

# Now let's save it
filtered_img.save('blur.png', 'png')

# NOTE: Keep in mind that .png supports image filters, .jpg doesn't

# Now let's convert the original pikachu to grayscale
gray_img = img.convert('L')
gray_img.save('grey_pikachu.png', 'png')

# We can also open it
gray_img.show()

# Other things we can do
rotated_img = img.rotate(90)
rotated_img.save('rotated_pikachu.png', 'png')

resized_gray_img = gray_img.resize((300, 300))
resized_gray_img.save('small_grey_pikachu.png', 'png')

box = (100, 100, 400, 400)
cropped_img = gray_img.crop(box)
cropped_img.save('cropped_pikachu.png', 'png')
