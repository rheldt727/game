import pygame, sys, math
from utilities.textures import *

pygame.init()

from utilities.spritesheet import *
pygame.mixer.music.load("/home/ryanh/Desktop/projgame/music/8-Bit Wii Shop Channel Music.wav")

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

def export_map(file):
    map_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / tile_size)) + "," + str(int(tile[1] / tile_size)) + ":" + tile[2] + "-"
        

    # Save Map Dimensions
    map_data = map_data + str(int(max_x / tile_size)) + "," + str(int(max_y / tile_size))


    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)

def load_map(file):
    global tile_data, tile_size
    with open(file, "r") as mapfile:
        map_data = mapfile.read()

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
        tiles[tiles.index(tile)] = [pos[0] * tile_size, pos[1] * tile_size, tile[1]]#save tile to list

    tile_data = tiles


window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

FPS = 60


txt_font = pygame.font.SysFont("comicsansms", 20)

TILESHEET = spritesheet("itemsheet.jpg", 64, 95)
CENTER_HANDLE = 0
index = 0

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * tile_size, 100 * tile_size


selector = pygame.Surface((tile_size, tile_size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(violet)

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "1234567890"



# Initialize Default Map
for x in range(0, map_width, tile_size):
    for y in range(0, map_height, tile_size):
        tile_data.append([x, y, "1"])
        




isRunning = True


while isRunning:
    pygame.mixer.music.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_r:
                brush = "r"
            elif event.key == pygame.K_t:
                selection = input("Brush Tag: ")
                brush = selection


            # SAVE MAP
            if event.key == pygame.K_c:
                name = raw_input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")

            #LOAD MAP
            elif event.key == pygame.K_l:
                name = raw_input("Map Name: ")
                load_map(name + ".map")
                print("Map Loaded Successfully!")


            

        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / tile_size) * tile_size
            mouse_y = math.floor(mouse_pos[1] / tile_size) * tile_size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, str(brush)]   # Keep this as a list

            # Is a tile already placed here?
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break

            # If this tile space is empty
            if not found:
                if not brush == "r":
                    tile_data.append(tile)
                    print(tile)

            # If this tile space is not empty
            else:
                # Are we using the rubber tool?
                if brush == "r":
                    # Remove Tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile Removed!")

                else:
                    print("A tile is already placed here!")
                            



    # LOGIC
    if camera_move == 1:
        camera_y += tile_size
    elif camera_move == 2:
        camera_y -= tile_size
    elif camera_move == 3:
        camera_x += tile_size
    elif camera_move == 4:
        camera_x -= tile_size



    # RENDER GRAPHICS

    window.fill(blue)


    # Draw Map
    for tile in tile_data:
        if tile[2] == "1":
            index = Grass()
            TILESHEET.draw(window, index%TILESHEET.totalCellCount, tile[0] + camera_x, tile[1] + camera_y, CENTER_HANDLE)
        elif tile[2] == "2":
            index = Stone()
            TILESHEET.draw(window, index%TILESHEET.totalCellCount, tile[0] + camera_x, tile[1] + camera_y, CENTER_HANDLE)
        elif tile[2] == "3":
            index = Water()
            TILESHEET.draw(window, index%TILESHEET.totalCellCount, tile[0] + camera_x, tile[1] + camera_y, CENTER_HANDLE)
        elif tile[2] == "0":
            index = Nothing()
            TILESHEET.draw(window, index%TILESHEET.totalCellCount, tile[0] + camera_x, tile[1] + camera_y, CENTER_HANDLE)
        


    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))
    
    

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
sys.exit()