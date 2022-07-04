#!/usr/bin/env python3


'''
This program was inspired by the Google Python Coursera course.
I wanted to just play around with my own code a little using the PIL module and Image object.
This program takes the image in the working directory named roatateimage and shows the image specifications.
The user is then prompted to provide a value for the new image size and a value in degrees for rotation.
The program will end with opening the image.

Roderick Davis

7/3/2022
'''


from PIL import Image
import os, sys

file = 'rotateimage.jpg'

im = Image.open(file).convert('RGB')

print('Image specs:\nFormat - {}\nSize - {}\nMode - {}'.format(im.format, im.size, im.mode))

resize = input('Do you want to resize the image? (Y/n)\n')

if resize == 'Y' or resize == 'y':
   x = int(input('New size (x): '))
   y = int(input('New size (y): '))
   newsize = (x, y)
   print('New size: ({}, {})'.format(x, y))
   im = im.resize(newsize)
elif resize != 'n' or resize != 'N':
   print('Please enter either Y or n')

rotate = input('Do you wan to rotate the image? (Y/n)\n')

if rotate == 'Y' or rotate == 'y':
   degrees = int(input('Degrees to rotate: '))
   im = im.rotate(degrees)
   print('Image rotated {} degrees'.format(str(degrees)))
elif rotate != 'N' or rotate != 'n':
   print('Please enter either Y or n, try again')

print('Here\'s your new image...')
im.show()

