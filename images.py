
# working with pixels
#  albert square
import sys, stddraw
from color import Color

r1 = int(9)
g1 = int(0)
b1 = int(0)
c1 = Color(r1, g1, b1)
r2 = int(100)
g2 = int(100)
b2 = int(100)
c2 = Color(r2, g2, b2)
stddraw.setCanvasSize(512, 256)
stddraw.setYscale(.25, .75)
stddraw.setPenColor(c1)
stddraw.filledSquare(.25, .5, .2)
stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .5, .1)
stddraw.setPenColor(c2)
stddraw.filledSquare(.75, .5, .2)
stddraw.setPenColor(c1)
stddraw.filledSquare(.75, .5, .1)
stddraw.show()


# compatibility of two colors
# this shows wether you can write one color on the other background 
# and have a clear text (greater than 128 is good)
import sys, stddraw
from color import Color

def luminance (c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()

    return (.299 * red) + (.587 * green) + (.114 * blue)


def compatible(c1, c2):
    return abs(luminance(c1)- luminance(c2))>=128.0


r1 = int(9)
g1 = int(90)
b1 = int(166)
c1 = Color(r1, g1, b1)
r2 = int(256)
g2 = int(256)
b2 = int(256)
c2 = Color(r2, g2, b2)
compatible(c1,c2)


# convert a color to grey

from color import Color
import sys, stddraw


def luminance (c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)


def toGray(c1):
    return Color(round(luminance(c1)), round(luminance(c1)), round(luminance(c1)))

r1 = int(9)
g1 = int(90)
b1 = int(166)
c1 = Color(r1, g1, b1)
c11 = toGray(c1)
# stddraw.setCanvasSize(512, 256)
# stddraw.setYscale(.25, .75)
# stddraw.setPenColor(c11)
# stddraw.filledSquare(.25, .5, .2)
# stddraw.show()

#working with image

# convert a colorful image to grey
from color import Color
import sys, stddraw
from picture import Picture

def luminance (c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)

def toGray(c1):
    return Color(round(luminance(c1)), round(luminance(c1)), round(luminance(c1)))

pic = Picture('sample.jpg')
width = pic.width()
height = pic.height()

for i in range(width):
    for j in range(height):
        alp = pic.get(i,j)
        pic.set(i,j, toGray(alp))

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()       

# resizing image

from color import Color
import sys, stddraw
from picture import Picture

w= 400
h= 200
source = Picture('sample.jpg')
target = Picture(w, h)
w_source = source.width()
h_source = source.height()

for i in range(w):
    for j in range(h):
        
        target.set(i,j, source.get(i*w_source//w, j*h_source//h))    


pic = target
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()       


