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