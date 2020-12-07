import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from enemy_bullet import EnemyBullet
from score import Score
from background import VertScrollBackground
import gobj
import enemy_gen
import life_gauge
import skill_gauge

canvas_width = 500
canvas_height = 800

def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui','e_bullet'])
    
    center = get_canvas_width() // 2, get_canvas_height() // 2
    bg = VertScrollBackground('bg_01.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg, bg)
    
    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    global score
    score = Score(canvas_width//2+40, canvas_height-20)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    life_gauge.load()
    skill_gauge.load()

def check_enemy(e):
    if gobj.collides_box(player, e):
        player.life-=50
        print('몬스터와 충돌 hp -50감소', e)
        e.remove()
        return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            dead = e.decrease_life(b.power)
            if dead:
                score.score += e.level * 10
                player.skill +=50
                e.remove()
            b.remove()
            return

def check_enemy_attack(eb):
    for eb in gfw.gfw.world.objects_at(gfw.layer.e_bullet):
        if gobj.collides_box(eb,player):
            player.life-=5
            eb.remove()
            return



def update():
    gfw.world.update()
    enemy_gen.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)
    for eb in gfw.world.objects_at(gfw.layer.e_bullet):
        check_enemy_attack(eb)



def draw():
    gfw.world.draw()
   
   

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
