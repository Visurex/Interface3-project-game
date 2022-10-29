import pygame

class Chest(pygame.sprite.Sprite):
	'''Creating a Enemy Sprite !'''
	def __init__(self,image,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.image = image
		self.rect  = self.image.get_rect(center = (pos_x,pos_y))

		self.chest_health = 100
		self.give_powerup = None
		self.give_health = None
		self.give_energy = None
		super().__init__()

	def chess_health(self):
		pass
	def energy(self):
		pass
	def health(self):
		pass
	def update_chest(self):
		pass
		self.chess_health()
		self.energy()
		self.health()




##	Row 00
#frame_chest_000 = SPR_S_CHEST.get_image( 0, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_001 = SPR_S_CHEST.get_image( 1, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_002 = SPR_S_CHEST.get_image( 2, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_003 = SPR_S_CHEST.get_image( 3, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_004 = SPR_S_CHEST.get_image( 4, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_005 = SPR_S_CHEST.get_image( 5, 0, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 01
#frame_chest_006 = SPR_S_CHEST.get_image( 0, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_007 = SPR_S_CHEST.get_image( 1, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_008 = SPR_S_CHEST.get_image( 2, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_009 = SPR_S_CHEST.get_image( 3, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_010 = SPR_S_CHEST.get_image( 4, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_011 = SPR_S_CHEST.get_image( 5, 1, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 02
#frame_chest_012 = SPR_S_CHEST.get_image( 0, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_013 = SPR_S_CHEST.get_image( 1, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_014 = SPR_S_CHEST.get_image( 2, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_015 = SPR_S_CHEST.get_image( 3, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_016 = SPR_S_CHEST.get_image( 4, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_017 = SPR_S_CHEST.get_image( 5, 2, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 03
#frame_chest_018 = SPR_S_CHEST.get_image( 0, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_019 = SPR_S_CHEST.get_image( 1, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_020 = SPR_S_CHEST.get_image( 2, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_021 = SPR_S_CHEST.get_image( 3, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_022 = SPR_S_CHEST.get_image( 4, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_023 = SPR_S_CHEST.get_image( 5, 3, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 04
#frame_chest_024 = SPR_S_CHEST.get_image( 0, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_025 = SPR_S_CHEST.get_image( 1, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_026 = SPR_S_CHEST.get_image( 2, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_027 = SPR_S_CHEST.get_image( 3, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_028 = SPR_S_CHEST.get_image( 4, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_029 = SPR_S_CHEST.get_image( 5, 4, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#
##	Row 05
#frame_chest_030 = SPR_S_CHEST.get_image( 0, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_031 = SPR_S_CHEST.get_image( 1, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_032 = SPR_S_CHEST.get_image( 2, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_033 = SPR_S_CHEST.get_image( 3, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_034 = SPR_S_CHEST.get_image( 4, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_035 = SPR_S_CHEST.get_image( 5, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 06
#frame_chest_036 = SPR_S_CHEST.get_image( 0, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_037 = SPR_S_CHEST.get_image( 1, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_038 = SPR_S_CHEST.get_image( 2, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_039 = SPR_S_CHEST.get_image( 3, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_040 = SPR_S_CHEST.get_image( 4, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_041 = SPR_S_CHEST.get_image( 5, 6, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
##	Row 07
#frame_chest_042 = SPR_S_CHEST.get_image( 0, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_043 = SPR_S_CHEST.get_image( 1, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_044 = SPR_S_CHEST.get_image( 2, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_045 = SPR_S_CHEST.get_image( 3, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_046 = SPR_S_CHEST.get_image( 4, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)
#frame_chest_047 = SPR_S_CHEST.get_image( 5, 7, SPR_C_WIDTH, SPR_C_HEIGHT, 1, BLACK)