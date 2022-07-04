#!/usr/bin/env python3

from PIL import Image
import os, sys

file = 'rotateimage.jpg'

im = Image.open(file).convert('RGB')

print('Image specs:\nFormat - {}\nSize - {}'.format(im.format, im.size))


x = int(input('New size (x): '))
y = int(input('New size (y): '))
newsize = (x, y)
degrees = int(input('Degrees to rotate (90, 180, 270): '))
im = im.resize(newsize).rotate(degrees)
im.show()

