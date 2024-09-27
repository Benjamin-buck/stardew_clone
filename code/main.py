# Import Pygame and Sys - Pygame to Run and Sys to be able to close the game.
import pygame, sys
from settings import *
from level import Level

# 
class Game:
	def __init__(self):
		# Initialize Pygame
		pygame.init()

		# Creating the game surface
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
		# Changes the title of the game window
		pygame.display.set_caption('SproutLand Valley')
		
		# Enabling the game clock
		self.clock = pygame.time.Clock()

		self.level = Level()

	def run(self):
		# Game Loop - Checking if the game is running and not closed.
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			# Delta Time
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()


# If we are in the main file, creating an object from the class and running the game method.
if __name__ == '__main__':
	game = Game()
	game.run()

