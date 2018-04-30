import pygame
from textures import *

def add_tile(tile, pos, addTo):
	addTo.blit(tile, (pos[0] * tile_size, pos[1] * tile_size))

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


	
	    	



