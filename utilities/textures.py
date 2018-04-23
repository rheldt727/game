
def Tile(self, name = None, index = None):
	if name == None:
		self.name = name
		self.raw = name.strip().lower()
	self.index = index
	

Grass = Tile("Grass", 589)

Stone = Tile("Stone", 460)

Water = Tile("Water", 281)


		
		

