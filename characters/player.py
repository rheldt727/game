
from character import *
from items.container import *

class Player(Character):
	def __init__(self, name, hp, s, i):
		Character.__init__(self, name, hp, s, i)
		self.s = s
		self.i = i
		self.inventory = Container("Inventory")

	def die(self, message = "Game Over!"):
		print(message)
		self.hp = 0
		self.dead = True
		input()



