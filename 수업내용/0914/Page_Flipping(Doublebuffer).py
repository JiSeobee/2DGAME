from pico2d import *
open_canvas()
grass = load_image('../res/grass.png')
character = load_image('../res/character.png')

x = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 85)
    update_canvas()
    get_events()
    x = x + 2
    delay(0.01)

close_canvas()
