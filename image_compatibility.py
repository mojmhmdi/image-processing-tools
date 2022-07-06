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
