commands = {
    'help': help,
    'exit': exit,
}

def help(player, args):
	for command in commands:
		print(command)

def exit(player, args):
	quit()
