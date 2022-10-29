import pygame
from Classes.spriteSheet import *

# sprite combine image and rectangle
# place sprites in grp or grpSingle
# draw/update all sprites in that group


#class Player(pygame.sprite.Sprite): 							# inherite from pygame.sprite.Sprite
#	def __init__(self):				 							# args
#		super().__init__()			 							#
#		self.image = pygame.image.load()						#needed sruf for sprite
#		self.rect  = self.image.get_rect(midbottom = 200,300)	#needed rect for sprite
#		self.gravity = 0
#
#	def apply_gravity():
#		pass
#	def player_input():
#		pass
#	def update(self):		 # update get called by player.update(in game loop) and update the class methods
#		self.player_input()  # calls method player_input
#		self.apply_gravity() # calls method apply_gravity

#player = pygame.sprite.GroupSingle()
#player.add(Player())
##game loop
#player.draw(screen)

		#		example of using floots for time passed
		#if player_rect.bottom < 300:
		#	player_surf = player_jump
		#else:
		#	player_index += 0.1
		#	if player_index >= len(player_walk):player_index = 0
		#	player_surf = player_walk[int(player_index)]

		#pass

class Player(pygame.sprite.Sprite):
	'''Player Class movement/animation !'''
	def __init__(self,pos_x,pos_y):
		# Create sprite related
		self.SPR_S_WIDTH  = 64
		self.SPR_S_HEIGHT = 64
		self.BLACK = (0,0,0)
		self.player_speed = 4
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.sprite_sheet_load = pygame.image.load(r"images/player_sheet.png").convert_alpha()
		self.sprite_sheet_player = SpriteSheet(self.sprite_sheet_load)
		self.image = self.sprite_sheet_player.get_image(0, 2, self.SPR_S_WIDTH, self.SPR_S_HEIGHT, 1, self.BLACK)
		self.rect  = self.image.get_rect(center = (pos_x,pos_y))
		#	Movement related
		self.counter = 0
		self.counter2 = 0
		#	Gameplay related
		self.health = None
		self.attack = None
		self.damage = None
		super().__init__()

	def player_movement(self):
		#	Keyboard input continious / movement animations
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.rect.x += self.player_speed
			self.counter += 0.1
			if self.counter >= 1:
				self.counter = 0
				self.image = self.sprite_sheet_player.get_image(self.counter2,11, self.SPR_S_WIDTH, self.SPR_S_HEIGHT, 1, self.BLACK)
				self.counter2 += 1
				if self.counter2 >= 8:
					self.counter2 = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_q]:
			self.rect.x -= self.player_speed
			self.counter += 0.1
			if self.counter >= 1:
				self.counter = 0
				self.image = self.sprite_sheet_player.get_image(self.counter2,9, self.SPR_S_WIDTH, self.SPR_S_HEIGHT, 1, self.BLACK)
				self.counter2 += 1
				if self.counter2 >= 8:
					self.counter2 = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.rect.y -= self.player_speed
			self.counter += 0.1
			if self.counter >= 1:
				self.counter = 0
				self.image = self.sprite_sheet_player.get_image(self.counter2,8, self.SPR_S_WIDTH, self.SPR_S_HEIGHT, 1, self.BLACK)
				self.counter2 += 1
				if self.counter2 >= 8:
					self.counter2 = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_s]:
			self.rect.y += self.player_speed
			self.counter += 0.1
			if self.counter >= 1:
				self.counter = 0
				self.image = self.sprite_sheet_player.get_image(self.counter2,10, self.SPR_S_WIDTH, self.SPR_S_HEIGHT, 1, self.BLACK)
				self.counter2 += 1
				if self.counter2 >= 8:
					self.counter2 = 0

		if keys[pygame.K_LSHIFT]:
			self.player_speed = 10
		else: 
			self.player_speed = 3

	def player_animation(self):
		pass
		
	def update_player(self):
		self.player_movement()
		self.player_animation()
