from pico2d import *
import gfw
from gobj import *

class LaserBullet:
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/Bullet_01.png')
        self.power = 50

    def draw(self):
        self.image.draw(self.x, self.y,30,30)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh
