import os, pygame, time, random, sys

pygame.init()

from commands import *
from characters.player import *
from utilities.util import *
from items.item import *
from items.weapon import *
from items.armor import *
from utilities.textures import *
from utilities.spritesheet import *


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

def create_window():
    global window, display_height, display_width, window_title
    display_width, display_height = 800, 600
    window_title = "First RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((display_width, display_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


#FPS

FPS = 60



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

#TEXTURES

TILESHEET = spritesheet("itemsheet.jpg", 64, 95)
CENTER_HANDLE = 0
index = 0

#MAP

def load_map(file):
    with open(file, "r") as mapfile:
        map_data = mapfile.read()

    #reading map file
    map_data = map_data.split("-")

    map_size = map_data[len(map_data) - 1] #map dimensions
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0]) * tile_size
    map_size[1] = int(map_size[1]) * tile_size

    global tiles 
    tiles = []

    for tile in range(len(map_data)):
        map_data[tile] = map_data[tile].replace("\n", "")
        tiles.append(map_data[tile].split(":"))             #split texture from position

    for tile in tiles:
        tile[0] = tile[0].split(",")#position into list
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p)#convert to int
        tiles[tiles.index(tile)] = (pos, tile[1])#save tile to list

    terrain = pygame.Surface(map_size, pygame.HWSURFACE)

    for tile in tiles:
        # if tile[1] in Texture_Tags:
        #   add_tile(Texture_Tags[tile[1]], tile[0], terrain)
        if int(tile[1]) == 1:
            index = Grass()
            TILESHEET.draw(terrain, index%TILESHEET.totalCellCount, tile[0][0] * tile_size, tile[0][1] * tile_size, CENTER_HANDLE)
        elif int(tile[1]) == 2:
            index = Stone()
            TILESHEET.draw(terrain, index%TILESHEET.totalCellCount, tile[0][0] * tile_size, tile[0][1] * tile_size, CENTER_HANDLE)
        elif int(tile[1]) == 3:
            index = Water()
            TILESHEET.draw(terrain, index%TILESHEET.totalCellCount, tile[0][0] * tile_size, tile[0][1] * tile_size, CENTER_HANDLE)
        elif int(tile[1]) == 0:
            index = Nothing()
            TILESHEET.draw(terrain, index%TILESHEET.totalCellCount, tile[0][0] * tile_size, tile[0][1] * tile_size, CENTER_HANDLE)

    return terrain

terrain = load_map("/home/ryanh/Desktop/projgame/maps/world.map")

# map_data = []
# for x in range(20):
#     for y in range(15):
#         map_data.append((x, y, "3"))
# for x in range(2, 18):
#     for y in range(2, 13):
#         map_data.append((x, y, "1"))

#GAME LOOP

Globes = Globals()


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                command_mode()
            elif event.key == pygame.K_p:
                pause()
            elif event.key == pygame.K_w:
                Globes.camera_move = 1
            elif event.key == pygame.K_s:
                Globes.camera_move = 2
            elif event.key == pygame.K_a:
                Globes.camera_move = 3
            elif event.key == pygame.K_d:
                Globes.camera_move = 4
        elif event.type == pygame.KEYUP:
            Globes.camera_move = 0

    #LOGIC
    if Globes.camera_move == 1:
        Globes.camera_y += 32
    elif Globes.camera_move == 2:
        Globes.camera_y -= 32
    elif Globes.camera_move == 3:
        Globes.camera_x += 32
    elif Globes.camera_move == 4:
        Globes.camera_x -= 32

    #RENDER
    window.fill(white)

    window.blit(terrain, (Globes.camera_x, Globes.camera_y))

    

    # - TILES
    # for x in range(0, 640, tile_size):
    #     for y in range(0, 480, tile_size):
    #         for i in map_data:
    #             tile = (i[0] * tile_size, i[1] * tile_size)
    #             if (x,y) == tile:
    #                 if (i[2]) == "1":
    #                     index = Grass()
    #                     TILESHEET.draw(window, index%TILESHEET.totalCellCount, x + Globes.camera_x, y + Globes.camera_y, CENTER_HANDLE)
    #                 elif (i[2]) == "2":
    #                     index = Stone()
    #                     TILESHEET.draw(window, index%TILESHEET.totalCellCount, x + Globes.camera_x, y + Globes.camera_y, CENTER_HANDLE)
    #                 elif (i[2]) == "3":
    #                     index = Water()
    #                     TILESHEET.draw(window, index%TILESHEET.totalCellCount, x + Globes.camera_x, y + Globes.camera_y, CENTER_HANDLE)
            

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
    







