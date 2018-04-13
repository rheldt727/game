
def help(player, args):
	for command in commands:
		print(command)

def exit(player, args):
	quit()

def inv(player, args):
	for name, item in player.inventory:
		print("{0}, x{1}".format(item.name, item.quantity))

def levl(player, args):
	pass
	'''print('Level:', lvl)
	print('Current XP:', xp)
	print('XP For Next Level:', lvlNext - xp)'''

def save(player, args):
	pass

def disp(player, args):
	pass

commands = {
    'help': help,
    'exit': exit,
    'inv': inv,
    'levl': levl,
    'save': save,
    'disp': disp,
}
