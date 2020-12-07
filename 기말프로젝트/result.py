from pico2d import *
import gfw
import gobj
import main_state
import menu
import score

canvas_width=500
canvas_height=800


def enter():
	global bg
	bg=load_image('res/bg_01.png')

	global font
	font = gfw.font.load(gobj.RES_DIR + '/ConsolaMalgun.ttf', 30)

	global result
	result=load_image('res/result.png')

	global result2
	result2=load_image('res/result01.png')

	global fail
	fail=load_image('res/fail.png')


	global result_bgm
	result_bgm=load_music('res/result.mp3')
	result_bgm.play()



def update():
	pass

def draw():
	bg.draw(canvas_width//2,canvas_height//2,500,800)
	result.draw(canvas_width//2,canvas_height-50,200,70)
	result2.draw(canvas_width-330,canvas_height//3-20,300,300)
	fail.draw(canvas_width//2,canvas_height-250,400,250)
	

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		gfw.quit()

def exit():
	global bg,result_bgm
	del bg,result_bgm




