
from character import Character

class Player(Character):
	def __init__(self, name, hp, s, i):
		Character.__init__(self, name, hp, s, i)
		self.s = s
		self.i = i



