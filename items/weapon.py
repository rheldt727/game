from item import *
import random

class Weapon(Item):
	def __init__(self, name, value, damage, quantity):
		Item.__init__(name, value, quantity)
		self.regDMG = damage[0]
		self.critDMG = damage[1]

	def damage(self):
		return random.randint(self.regDMG, self.critDMG)

class WeaponEnhanced(Weapon):
	def __init__(self, name, value, damage, enhancement, quantity):
		Weapon.__init__(name, value, quantity, damage)
		self.enhancement = enhancement

