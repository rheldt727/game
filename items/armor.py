from item import *

class Armor(Item):
	def __init__(self, name, value, armor, quantity):
		Item.__init__(name, value, quantity)
		self.armor = armor