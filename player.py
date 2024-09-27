import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# General Setup
		self.image = pygame.Surface((32, 64))
		self.image.fill('green')
		self.rect = self.image.get_rect(center = pos)

		# Movement Attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200


	def input(self):
		# gets all the keys that are being pressed.
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else: 
			self.direction.y = 0
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else: 
			self.direction.x = 0

	def move(self, dt):
		self.pos += self.direction * self.speed * dt
		self.rect.center = self.pos


	def update(self, dt): 
		self.input()
		self.move(dt)