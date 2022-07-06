
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