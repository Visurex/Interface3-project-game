import pygame

class Display:
	def __init__(self,screen):
		self.screen = screen
		self.test_font = pygame.font.Font(pygame.font.get_default_font(),20)
	def display_title(self):
		#	Game name
		game_name_surf = self.test_font.render("My Game Project",True,(255,0,0))
		game_name_rect = game_name_surf.get_rect(center = (625,90))
		#	Blit
		self.screen.blit(game_name_surf,game_name_rect)
	
	def display_time(self):
				#	Game score
		current_time = pygame.time.get_ticks()
		current_time_surf = self.test_font.render(f"Sec: {str(current_time//600)}",True, "white")
		current_time_rect = current_time_surf.get_rect(center = (1205,50))
		self.screen.blit(current_time_surf,current_time_rect)