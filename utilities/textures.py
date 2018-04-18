import pygame
from spritesheet import *

pygame.init()

class Tiles:
	
	Size = 32

	def Load_Texture(index, Size):
		TILESHEET = spritesheet("itemsheet", 64, 95)
		CENTER_HANDLE = 0

		bitmap = 
		
		bitmap = pygame.transform.scale(bitmap, (Size, Size))
		surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
		surface.blit(bitmap, (0, 0))
		return surface

	
