from __future__ import print_function
from PIL import Image, ImageFilter
import numpy as np
import math
import os
import sys

f = open('RGB.txt', 'a')
#def sumrgb(image):
    R=0
    G=0
    B=0
    im = Image.open('hao.jpg')
    pix = im.load()
    width, height = im.size
    print(width,height)
    for i in range(width):
        for j in range(height):
            R+=pix[i,j][0]
            G+=pix[i,j][1]
            B+=pix[i,j][2]
    f.write('%d %d %d'%(R,G,B)+'\n')
print (im.size[0],im.size,im.mode)
'''
print (im.size[0],im.size,im.mode)
r,g,b = im.split()
red=r.save('R.jpg','JPEG')
green=g.save('G.jpg','JPEG')
blue=b.save('B.jpg','JPEG')

#pix=red.load()
#print pix

#print (R)
'''