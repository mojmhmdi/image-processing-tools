
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
