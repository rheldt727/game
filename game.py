'''import os
import pygame
import time
import random'''
import sys


from commands import *
from player import *
from util import *

commands = {
    'help': help,
    'exit': exit,
}

player = Player("Default", 1, 1, 1)

def nameInput(prompt):
	name = input(prompt)
	return name.strip()

def getName():
	tempName = ""
	while 1:
		tempName = nameInput("What is your name? ")
		if len(tempName) < 1:
			continue
		yes = yesOrNo(tempName + ", is that your name?")

		if yes:
			return tempName
		else:
			continue

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False


def runCMD(cmd, args, player):
    commands[cmd](player, args)

def main(player):
    player.name = getName()

    while (not player.dead):
        line = raw_input(">> ")
        input = line.split()
        input.append("EOI")
        if isValidCMD(input[0]):
            runCMD(input[0], input[1], player)

main(player)   



#pygame.init()

'''#colors
white = (255,255,255)
black = (0,0,0)
red = (240,32,32)
orange = (255,150,0)
yellow = (234,237,27)
green = (0,203,42)
blue = (0,61,204)
indigo = (29,0,51)
violet = (138,43,226)

#display
display_width = 1920
display_height = 1080
gameDisplay = pygame.display.set_mode((display_width, display_height))

#game stuff
pygame.display.set_caption('Big Guy Lil Sword')
icon = pygame.image.load('')
pygame.display.set_icon(icon)

#variables
clock = pygame.time.Clock()


#sprites


#functions

#text objects
def text_objects(text,color,size):
    if size == "small":
    	textSurface = smallfont.render(text, True, color)
    elif size == "med":
    	textSurface = medfont.render(text, True, color)
    elif size == "large":
    	textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
     
#message
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

#intro
def gameStart():
    intro = True
    while intro == True:

        for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
        	pygame.quit()
        	quit()
            if event.type == pygame.KEYDOWN:
        	intro = False    


    	gameDisplay.fill(white)
    	pygame.display.update()
    	clock.tick(15)
    

#pause
def pause():
    pause = True
    while paused:
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
        	pygame.quit()
        	quit()
            if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_p:
            	    paused = False
	message_to_screen("PAUSED", black, 0, "large")
        pygame.display.update()
        clock.tick(5)

#game Loop
def gameLoop():'''
    







