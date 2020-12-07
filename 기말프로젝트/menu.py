from pico2d import *
import gfw
import gobj
import main_state

canvas_width=main_state.canvas_width
canvas_height=main_state.canvas_height 


def enter():
	global bg
	bg = load_image('res/DF_menu.png')

	global font
	font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 30)

	global music_bg
	music_bg=load_music('res/dragon_flight2.mp3')
	music_bg.play()


def update():
	pass

def draw():
	bg.draw(canvas_width//2,canvas_height//2,500,800)
	color = (205,12,34)
	color2= (255,255,0)
	font.draw(50,canvas_height//10,'<<Press Spacebar button>>',color)
	font.draw(50,canvas_height//11,'<<Press Spacebar button>>',color2)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		gfw.quit()
	elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
		music_bg.stop()
		gfw.push(main_state)

def exit():
	global bg, music_bg
	del bg
	del music_bg

def pause():
	pass

def resume():
	pass

if __name__ == '__main__':
	gfw.run_main()

