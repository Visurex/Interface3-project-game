import pygame

pygame.init()
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Interface 3 Projet de jeux !")
clock = pygame.time.Clock()

test_surf = pygame.Surface((100,200))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


	pygame.display.update()
	clock.tick(60) 