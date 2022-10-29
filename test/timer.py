import pygame

pygame.init()

SCREEN_W = 800
SCREEN_H = 600


screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Interface 3 Projet de jeux !")
clock = pygame.time.Clock()

test_surf = pygame.Surface((100,200))
test_surf.fill("red")

obstacle_timer = pygame.USEREVENT + 1 # create custom event
pygame.time.set_timer(obstacle_timer,900) # ms

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == obstacle_timer:
        print("test")


    pygame.display.update()
    clock.tick(60) 