from pico2d import *
open_canvas()

grass = load_image('../res/grass.png')
character = load_image('../res/animation_sheet.png')

x = 0
frame_index=0
action=0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100*frame_index,100*action,100,100,x, 85)
    update_canvas()
    get_events()
    x = x + 2
    if x % 100 == 0:
        action = (action +1) % 4
    frame_index=(frame_index +1) % 8
    delay(0.01)

close_canvas()
