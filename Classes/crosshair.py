import pygame

class CrossHair:
	'''Creating a Crosshair for mouse position !'''
	color = "red"
	def __init__(self,screen,mouse_pos):
		self.screen = screen
		self.mouse_pos = mouse_pos
	
	def cross_hair(self):
		cross_hair = pygame.draw.circle(self.screen, self.color,self.mouse_pos,10, width = 3)
		return cross_hair