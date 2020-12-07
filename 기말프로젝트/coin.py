from pico2d import *
import gfw
from gobj import *

class Coin:
	Size = 40
	def __init__(self,x,y,speed):
		self.x,self.y= x, y
		self.dy=speed
		self.image=gfw.image.load(RES_DIR + '/coin.png')
		

	def draw(self):
		self.image.draw(self.x,self.y,40,40)

	def update(self):
		self.y -=self.dy * gfw.delta_time
		if self.y < 0 + Coin.Size:
			self.remove()

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		hw = self.image.w // 2
		hh = self.image.h // 2
		return self.x - hw, self.y - hh, self.x + hw, self.y + hh





