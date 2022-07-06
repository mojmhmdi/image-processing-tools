
# transfomrs the source image to three image using filters
from color import Color
import sys, stddraw
from picture import Picture

def main():
    source = Picture('sample.jpg')
    w = source.width()
    h = source.height()
    target_blue = Picture(w,h)
    target_green = Picture(w,h)
    target_red = Picture(w,h)


    for i in range(w):
        for j in range(h):
            pixel = source.get(i,j)
            red_value = pixel.getRed()
            blue_value = pixel.getBlue()
            green_value = pixel.getGreen()
            
            target_pixel_red = Color(red_value,0,0)
            target_pixel_blue = Color(0,0,blue_value)
            target_pixel_green = Color(0,green_value,0)
            
            target_red.set(i,j, target_pixel_red)
            target_blue.set(i,j, target_pixel_blue)
            target_green.set(i,j, target_pixel_green)
    return target_red, target_blue, target_green

target_red, target_blue, target_green = main()   

pic = target_red
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show(2000) 

pic = target_blue
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show(2000)

pic = target_green
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show(2000)



