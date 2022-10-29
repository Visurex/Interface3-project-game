import pygame

class Enemy(pygame.sprite.Sprite):
	'''Creating a Enemy Sprite !'''
	def __init__(self,image,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.image = image
		self.rect  = self.image.get_rect(center = (pos_x,pos_y))

		self.healt = None
		self.attack = None
		self.damage = None
		super().__init__()