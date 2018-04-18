import os, pygame, time, random, sys
from commands import *
from player import *
from util import *
from item import *
from weapon import *
from armor import *
from spritesheet import *

commands = {
        'help': help,
        'exit': exit,
        'inv': inv,
        'levl': levl,
        'save': save,
        'disp': disp,
    }

#CLRS
white = (255,255,255)
black = (0,0,0)
red = (240,32,32)
orange = (255,150,0)
yellow = (234,237,27)
green = (0,203,42)
blue = (0,61,204)
indigo = (29,0,51)
violet = (138,43,226)

pygame.init()

#MSG TO WINDOW

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 45)
largefont = pygame.font.SysFont("comicsansms", 65)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "med":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    window.blit(textSurf, textRect)

#WINDOW

tile_size = 32

def create_window():
    global window, display_height, display_width, window_title
    display_width, display_height = 800, 600
    window_title = "First RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((display_width, display_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


#FPS

FPS = 60
'''cSec = 0
cFrame = 0

def fps_wind():
    text_fps = smallfont.render(str(FPS), True, black)
    window.blit(text_fps, [0,0])

def fps_rate():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")'''

#MODES

def command_mode():
    command_prompted = True
    while command_prompted:
        message_to_screen("COMMAND MODE", black, 0, "large")
        pygame.display.update()
        line = raw_input(">> ")
        input = line.split()
        input.append("EOI")
        if isValidCMD(input[0]):
            runCMD(input[0], input[1], player)
        yes = yesOrNo("Continue using cm? ")

        if yes:
            continue
        else:
            command_prompted = False
        clock.tick(5)

def pause():
    paused = True
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

#GETNAME FUNCS

def nameInput(prompt):
        name = raw_input(prompt)
        return name

def getName():
        Name = ""
        while 1:
            Name = nameInput("What is your name? ")
            if len(Name) < 2:
                continue
            yes = yesOrNo(Name + ", is that your name? ")

            if yes:
                return Name
            else:
                continue

#CMD FUNCS

def isValidCMD(cmd):
        if cmd in commands:
            return True
        return False

def runCMD(cmd, args, player):
        commands[cmd](player, args)

player = Player("Default", 1, 1, 1)

clock = pygame.time.Clock()

isRunning = True

player.name = getName()

create_window()

#GAME LOOP

while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                command_mode()
            if event.key == pygame.K_p:
                pause()

    #LOGIC

    #RENDER
    window.fill(white)

    # - TILES
    for x in range(0, 640, tile_size):
        for y in range(0, 480, tile_size):
            pygame.draw.rect(window, black, (x, y, tile_size + 1, tile_size + 1), 1)

    pygame.display.update()

    clock.tick(FPS)
   
pygame.quit()
sys.exit()






'''#display
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
    







