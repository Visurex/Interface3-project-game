import pygame

class Dungeon(pygame.sprite.Sprite):
	'''Creating a Dungeon Sprites !'''
	def __init__(self,image,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.image = image
		self.rect  = self.image.get_rect(center = (pos_x,pos_y))

		self.wall_health = None
		super().__init__()

	#def create_walls():
		#for _ in range(14):
		#	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_WIDTH,WALL_SIZE)
		#	wall_list_up.append(dungeon_wall)
		#for _ in range(13):
		#	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_WIDTH,WALL_SIZE)
		#	wall_list_down.append(dungeon_wall)
		#for _ in range(7):
		#	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_SIZE,WALL_WIDTH)
		#	wall_list_left.append(dungeon_wall)
		#for _ in range(7):
		#	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_SIZE,WALL_WIDTH)
		#	wall_list_right.append(dungeon_wall)
		#for walls in wall_list_up:
		#	walls.rect[0] *= counter_wall
		#	sprite_group_dungeon.add(walls)
		#	counter_wall += 1
		#for walls2 in wall_list_down:
		#	walls2.rect[0] *= counter_wall2 
		#	walls2.rect[1] += 740
		#	sprite_group_dungeon.add(walls2)
		#	counter_wall2 += 1
		#for walls3 in wall_list_left:
		#	walls3.rect[1] *= counter_wall3 
		#	walls3.rect[0] += 0
		#	walls3.image = pygame.transform.rotate(walls3.image,90)
		#	walls.rect.x += 10
		#	sprite_group_dungeon.add(walls3)
		#	counter_wall3 += 1
		#for walls4 in wall_list_right:
		#	walls4.rect[1] *= counter_wall4
		#	walls4.rect[0] += 1190
		#	walls4.image = pygame.transform.rotate(walls4.image,-90)
		#	walls.rect.x += 10
		#	sprite_group_dungeon.add(walls4)
		#	counter_wall4 += 1