import pygame
from textures import *

def add_tile(tile, pos, addTo):
	addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))

def load_map(file):
    with open(file, "r") as mapfile:
    	map_data = mapfile.read()

	#reading map file
	map_data = map_data.split("-")

	map_size = map_data[len(map_data) - 1] #map dimensions
	map_data.remove(map_size)
	map_size = map_size.splt(",")
	map_size[0] = int(map_size[0]) * tile_size
	map_size[1] = int(map_size[1]) * tile_size

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
		if tile[1] == 1:
			#add_tile(Texture_Tags[tile[1]], tile[0])
			Grass()
			TILESHEET.draw(window, index%TILESHEET.totalCellCount, pos[0] * Tiles.Size, pos[1] * Tiles.Size, CENTER_HANDLE)

