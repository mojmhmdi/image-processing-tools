
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