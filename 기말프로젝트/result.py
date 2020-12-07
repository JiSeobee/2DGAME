from pico2d import *
import gfw
import gobj
import main_state
import highscore

canvas_width=main_state.canvas_width
canvas_height=main_state.canvas_height 

def enter():
	global bg
	bg=load_image('res/bg_01.png')

	global font
	font = gfw.font.load(gobj.RES_DIR + '/ConsolaMalgun.ttf', 30)

	global result
	result=load_image('res/result.png')

	global result2
	result2=load_image('res/result01.png')

	global high_score
	high_score=load_image('res/high_score.png')

	global score
	score=load_image('res/result_rs.png')

	highscore.add(score)
	gfw.world.add(gfw.layer.ui,highscore)
	highscore.load()

def update():
	pass

def draw():
	bg.draw(canvas_width//2,canvas_height//2,500,800)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		gfw.quit()

def exit():
	global bg
	del bg




