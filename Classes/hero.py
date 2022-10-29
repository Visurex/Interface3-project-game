import pygame

class Hero(pygame.sprite.Sprite):
	'''Creating a Hero Sprite !'''
	def __init__(self):
		self.image = pygame.image.load("images/hero.png")
		self.rect  = self.image.get_rect(center = (200,300))
		super().__init__()