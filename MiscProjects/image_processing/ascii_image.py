from PIL import Image
import numpy
import sys

im = Image.open("white_doggo.jpeg")

print(im.size)

numpy.array(im.getdata())
