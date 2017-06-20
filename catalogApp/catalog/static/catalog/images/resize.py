from PIL import Image

import os, sys


path="noImageAvailable.png"
im = Image.open("noImageAvailable.png")
new_size = 130, 130
im.thumbnail(new_size, Image.ANTIALIAS)
im.save("new"+path)
