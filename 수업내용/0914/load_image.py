from pico2d import *

open_canvas()

ch=load_image('../res/character.png')
ch.draw_now(200,400)

for y in range(100,501,100):
    for x in range(100,701,100):
        ch.draw_now(x,y)

delay(5)

close_canvas()
