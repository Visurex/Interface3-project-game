import pygame
from random import randint

class Bullet:
	'''Creating a Bullet ! Then move it !'''
	def __init__(self,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.color = (randint(0,255),randint(0,255),randint(0,255))
		self.bullet_width = 13
		self.bullet_height = 8
		self.velocity_x = -4
		self.velocity_y = 0
		
	def create_bullet(self):
			#	Bullet
		bullet_surf = pygame.Surface((self.bullet_width,self.bullet_height))
		bullet_rect = bullet_surf.get_rect(center = (self.pos_x,self.pos_y))
			#	Bullet Sprite
		bullet_sprite = pygame.sprite.Sprite()
		bullet_sprite.image = bullet_surf
		bullet_sprite.rect = bullet_rect
		bullet_sprite.image.fill(self.color)
		return bullet_sprite

	def bullet_move(self,sprites):
		sprites.rect.x += self.velocity_x  
		sprites.rect.y += self.velocity_y 
		

	#def bullet_fire(SCREEN_W,SCREEN_H,fire_bullet,bullets,hero_sprite,enemy_spirte,bullet_destroy):
	#	bullet_destroy = []
	#	if fire_bullet == True:
	#		if bullets.rect.x > SCREEN_W or bullets.rect.x < 0 :
	#				bullet_destroy.append(bullets)
	#		elif bullets.rect.y > SCREEN_H or bullets.rect.y < 0 :
	#				bullet_destroy.append(bullets)
	#		elif bullets.rect.colliderect(hero_sprite.rect):
	#				bullet_destroy.append(bullets)
	#		elif bullets.rect.colliderect(enemy_spirte.rect):
	#				bullet_destroy.append(bullets)
	#	
	#	bullet_destroy = Bullet.bullet_fire(SCREEN_W,SCREEN_H,fire_bullet,bullets,hero_sprite,enemy_spirte,bullet_destroy)
