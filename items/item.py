class Item(object):
	def __init__(self, name, value, quantity=1):
		self.name = name
		self.raw = name.strip().lower()
		self.quantity = quantity
		self.value = value
		self.netValue = value * quantity
	
	def recalc(self):
		self.netValue = self.value * self.quantity
		


