from PIL import ImageFilter, Image

img = Image.open('./astro.jpg')
print(img.size)  # (5611, 5339)
img.thumbnail((400, 400))
img.save('astro_thumbnail.jpg')
