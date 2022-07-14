#!/bin/python3

from PIL import Image

png = input("path to PNG > ")

out = png[:-4]  + ".pdf"

image_1 = Image.open(png)
im_1 = image_1.convert('RGB')
im_1.save(out)
