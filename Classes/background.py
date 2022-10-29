import pygame

class Background: 
    def __init__(self,width,height):
        self.BG_IMG_STONE = pygame.image.load(r"images/stone.png").convert()
        self.BG_SIZE  = 512
        self.SCREEN_W = width
        self.SCREEN_H = height
        self.screen = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H))

    def create_background(self):
                #	Background Image
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE-self.BG_SIZE,self.BG_SIZE-self.BG_SIZE))
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE,self.BG_SIZE))
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE,self.BG_SIZE-self.BG_SIZE))
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE-self.BG_SIZE,self.BG_SIZE))
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE*2,self.BG_SIZE-self.BG_SIZE))
        self.screen.blit(self.BG_IMG_STONE,(self.BG_SIZE*2,self.BG_SIZE))
