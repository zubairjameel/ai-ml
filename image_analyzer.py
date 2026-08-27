import numpy as np
from PIL import Image, ImageOps

img = Image.open("free-nature-images.jpg").convert("L")
img_array = np.array(img)
print(img_array)
inverted = 255 - img_array
inverted = Image.fromarray(inverted)
inverted.save("inverted.jpg")