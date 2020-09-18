from pico2d import *

open_canvas()

grass = load_image('../res/grass.png')
ch = load_image('../res/character.png')

x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    ch.draw_now(x,85)
    x=x+2
    delay(0.01)

close_canvas()
    

