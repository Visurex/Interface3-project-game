import pygame
from Classes.hero import *
from Classes.chest import *
from Classes.enemy import *
from Classes.player import *
from Classes.bullet import *
from Classes.display import *
from Classes.dungeon import *
from Classes.crosshair import *
from Classes.background import *
from Classes.spriteSheet import *
from sys import exit

	#	Pygame initiation
pygame.init()
pygame.display.set_caption("Interface 3 Projet de jeux !") 

	#	Sceen display
SCREEN_W = 1250
SCREEN_H = 800
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
clock = pygame.time.Clock()

	#	Constant Variables
BLACK 		 = (0,0,0)
SPR_S_WIDTH  = 65
SPR_S_HEIGHT = 65
SPR_C_WIDTH  = 39
SPR_C_HEIGHT = 39
SPR_D_WIDTH  = 128
SPR_D_HEIGHT = 128
WALL_SIZE    = 30
WALL_WIDTH	 = 134
	#	Sprite Sheets Vars
SPR_S_E_LOAD 	= pygame.image.load(r"images/enemy.png").convert_alpha()
SPR_S_C_LOAD 	= pygame.image.load(r"images/chest.png").convert_alpha()
SPR_S_D_LOAD 	= pygame.image.load(r"images/Dungeon_Tileset.png").convert_alpha()
SPR_S_ENEMY  	= SpriteSheet(SPR_S_E_LOAD)
SPR_S_CHEST  	= SpriteSheet(SPR_S_C_LOAD)
SPR_S_DUNGEON   = SpriteSheet(SPR_S_D_LOAD)
#	----------------- global vars -----------------
#	Sprites Sheet Vars
#frame_player_000  			= SPR_S_PLAYER.get_image( 0, 2, SPR_S_WIDTH, SPR_S_HEIGHT, 1, BLACK)
frame_enemy_000   			= SPR_S_ENEMY.get_image( 0, 0, SPR_S_WIDTH, SPR_S_HEIGHT, 1, BLACK)
frame_chest_052   			= SPR_S_CHEST.get_image( 2, 5, SPR_C_WIDTH, SPR_C_HEIGHT, 1.1, BLACK)
frame_dungeon_sqrwall 		= SPR_S_DUNGEON.get_image( 0, 0, 90, 125, 1.1, BLACK)
frame_dungeon_linewall_up 	= SPR_S_DUNGEON.get_image( 5, 1, 65, 60, 1.5, BLACK)
frame_dungeon_linewall_down = SPR_S_DUNGEON.get_image( 5, 1, 65, 60, 1.5, BLACK)

	#	bool
game_active = True
fire_bullet = False
	#	list
bullet_list = []
wall_list_up = []
wall_list_down = []
wall_list_left = []
wall_list_right = []
	#	Values
counter_wall = 1
counter_wall2 = 1
counter_wall3 = 1
counter_wall4 = 1
#	!!!!!!!!!!!! SPRITES !!!!!!!!!!!!
player_spirte = Player(SCREEN_W/2,SCREEN_H/2)
enemy_spirte  = Enemy(frame_enemy_000,SCREEN_W/2 -200,SCREEN_H/2)
chest_spirte  = Chest(frame_chest_052,SCREEN_W/2 -150,SCREEN_H/2 -300)
hero_sprite	  = Hero()
#		Square wall corners !
dungeon_spirte  = Dungeon(frame_dungeon_sqrwall,40,57)
dungeon_spirte1 = Dungeon(frame_dungeon_sqrwall,1202,57)
dungeon_spirte2 = Dungeon(frame_dungeon_sqrwall,1202,734)
dungeon_spirte3 = Dungeon(frame_dungeon_sqrwall,40,734)
#	!!!!!!!!! GROUPS !!!!!!!!!!!!!
#			Create groups
sprite_group_hero    = pygame.sprite.GroupSingle()
sprite_group_player  = pygame.sprite.GroupSingle()
sprite_group_dungeon = pygame.sprite.Group()
sprite_group_enemy   = pygame.sprite.Group()
sprite_group_bullet  = pygame.sprite.Group()
sprite_group_chess   = pygame.sprite.Group()
#			add to groups
sprite_group_hero    . add(hero_sprite)
sprite_group_player  . add(player_spirte)
sprite_group_enemy   . add(enemy_spirte)
sprite_group_chess   . add(chest_spirte)

#	!!!!!!!!!!!!!!Create Walls with dungeon sprite sheet !!!!!!!!!!!!!!!!
for _ in range(14):
	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_WIDTH,WALL_SIZE)
	wall_list_up.append(dungeon_wall)
for _ in range(13):
	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_WIDTH,WALL_SIZE)
	wall_list_down.append(dungeon_wall)
for _ in range(7):
	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_SIZE,WALL_WIDTH)
	wall_list_left.append(dungeon_wall)
for _ in range(7):
	dungeon_wall = Dungeon(frame_dungeon_linewall_up,WALL_SIZE,WALL_WIDTH)
	wall_list_right.append(dungeon_wall)
for walls in wall_list_up:
	walls.rect[0] *= counter_wall
	sprite_group_dungeon.add(walls)
	counter_wall += 1
for walls2 in wall_list_down:
	walls2.rect[0] *= counter_wall2 
	walls2.rect[1] += 740
	sprite_group_dungeon.add(walls2)
	counter_wall2 += 1
for walls3 in wall_list_left:
	walls3.rect[1] *= counter_wall3 
	walls3.rect[0] += 0
	walls3.image = pygame.transform.rotate(walls3.image,90)
	walls.rect.x += 10
	sprite_group_dungeon.add(walls3)
	counter_wall3 += 1
for walls4 in wall_list_right:
	walls4.rect[1] *= counter_wall4
	walls4.rect[0] += 1190
	walls4.image = pygame.transform.rotate(walls4.image,-90)
	walls.rect.x += 10
	sprite_group_dungeon.add(walls4)
	counter_wall4 += 1
#	add dungeon sprite to group
sprite_group_dungeon . add(dungeon_spirte)
sprite_group_dungeon . add(dungeon_spirte1)
sprite_group_dungeon . add(dungeon_spirte2)
sprite_group_dungeon . add(dungeon_spirte3)

while True:
		#	Mouse Position
	mouse_pos = pygame.mouse.get_pos()
		#	Event handerler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			fire_bullet = True
			bullet = Bullet(player_spirte.rect.x,player_spirte.rect.y)
			bullet_sprite = bullet.create_bullet()
			bullet_list.append(bullet_sprite)

	bullet_destroy = []
	if fire_bullet == True:
		for bullets in bullet_list:
			sprite_group_bullet.add(bullets)
			bullet.bullet_move(bullets)
			if bullets.rect.x > SCREEN_W or bullets.rect.x < 0 :
					bullet_destroy.append(bullets)
			elif bullets.rect.y > SCREEN_H or bullets.rect.y < 0 :
					bullet_destroy.append(bullets)
			elif bullets.rect.colliderect(hero_sprite.rect):
					bullet_destroy.append(bullets)
			elif bullets.rect.colliderect(enemy_spirte.rect):
					bullet_destroy.append(bullets)
		for bullets in bullet_destroy:
			if bullet_list.remove(bullets):
				pass
			if sprite_group_bullet.remove(bullets):
				pass

	#	Groupe Collision
	pygame.sprite.groupcollide(sprite_group_dungeon,sprite_group_bullet,True,True)

#----------------- WORK OK----------------------------
	#	Background Image
	Background(SCREEN_W,SCREEN_H).create_background()
	#	Player update 
	player_spirte.update_player()
	#	Sprite group DRAW / UPDATE!
	sprite_group_bullet	.draw(screen)
	sprite_group_dungeon.draw(screen)
	sprite_group_chess	.draw(screen)
	sprite_group_hero	.draw(screen)
	sprite_group_enemy	.draw(screen)
	sprite_group_player	.draw(screen)
	sprite_group_dungeon.update()
	sprite_group_player	.update()
	sprite_group_enemy	.update()
	sprite_group_hero	.update()
	sprite_group_chess	.update()
	sprite_group_bullet	.update()

	#	Display title
	Display(screen).display_title()
	#	Display time passed
	Display(screen).display_time()
	#	Set Crosshair
	CrossHair(screen,mouse_pos).cross_hair()
	#	Mouse set Invisible
	pygame.mouse.set_visible(False)

	# -------- DEBUG --------
	#	show fps
	#print(int(clock.get_fps()))
	#	print bullet list len()
	#print(len(bullet_list))
	#	print sprite in group
	#print(sprite_group_bullet.sprites)
	#print(sprite_group_dungeon.sprites)
	#print(sprite_group_player.sprites)
	#print(sprite_group_enemy.sprites)
	#print(sprite_group_hero.sprites)
	#print(sprite_group_chess.sprites)
	#	print mouse position
	#print(mouse_pos)
	#	Update & Clock
	pygame.display.update()
	clock.tick(60)
