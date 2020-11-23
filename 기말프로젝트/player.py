import random
from pico2d import *
import gfw
from gobj import *
from bullet import *
import life_gauge
import skill_gauge

class Player:
    speed=320
    LASER_INTERVAL = 0.15
    SPARK_OFFSET = 28

    def __init__(self):
        self.x, self.y = 250, 80
        self.dx = 0
        self.speed = 320
        self.max_life = 300
        self.life = self.max_life
        self.max_skill_guage = 1000
        self.skill = 0
        self.image = gfw.image.load(RES_DIR + '/player.png')
        self.laser_time = 0

    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y + Player.SPARK_OFFSET, 400)
        gfw.world.add(gfw.layer.bullet, bullet)

    def draw(self):
        self.image.draw(self.x, self.y,90,90)
        rate = self.life / self.max_life
        life_gauge.draw(self.x,self.y//2,80,rate)
        
        skill_rate = self.skill / self.max_skill_guage
        skill_gauge.draw(250,self.y//4,160,skill_rate)

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time
        self.x = clamp(self.image.w//4, self.x, get_canvas_width()-self.image.w//4)
        self.laser_time += gfw.delta_time
        if self.laser_time >= Player.LASER_INTERVAL:
            self.fire()
            
        if self.life<=0:
            gfw.quit()

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key==SDLK_LEFT:
                self.dx-=1
            elif e.key == SDLK_RIGHT:
                self.dx+=1

        elif e.type == SDL_KEYUP:
            if e.key==SDLK_LEFT:
                self.dx+=1
            elif e.key == SDLK_RIGHT:
                self.dx-=1

    def remove(self):
        gfw.world.remove(player)


    def get_bb(self):
        hw = self.image.w / 4
        hh = self.image.h / 4
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh


if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RECTS:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2
        print('(%3d, %d, %d, %d),' % (l,t,r,b))
