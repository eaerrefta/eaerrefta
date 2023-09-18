import pygame
from pygame.locals import *
import spritesheet
import random

#Hippo class
class Hippo(pygame.sprite.Sprite):
	def __init__(self, surf, scale=1):
		pygame.sprite.Sprite.__init__(self)
		sprite_sheet_image = pygame.image.load("images/hippo.png").convert_alpha()
		sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
		self.masterImage = sprite_sheet.get_image(0, 24, 24, scale, (0,0,0)).convert_alpha()
		self.image = self.masterImage
		self.rect = self.image.get_rect()
		self.moveVector = pygame.Vector2(0,0)
		self.mask = pygame.mask.from_surface(self.image)
		self.surfSize = surf.get_size()
		self.pos = (self.surfSize[0]/2,self.surfSize[1]/2)
		self.rect.center = self.pos
		self.rotationAngle = 0
		self.upVector = pygame.Vector2(0, -1)

	def vectorUpdate(self, inputVector):
		self.moveVector += inputVector
		if inputVector[0] != 0 or inputVector[1] != 0:
			self.rotationAngle = self.upVector.angle_to((self.moveVector[0]*-1,self.moveVector[1]))

	def update(self):
		self.image = pygame.transform.rotate(self.masterImage, self.rotationAngle).convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.pos += self.moveVector
		if self.pos[0] < 0:
			self.pos[0] = 0
		if self.pos[0] > self.surfSize[0]:
			self.pos[0] = self.surfSize[0]
		if self.pos[1] < 0:
			self.pos[1] = 0
		if self.pos[1] > self.surfSize[1]:
			self.pos[1] = self.surfSize[1]
		self.rect.center = self.pos
		self.moveVector = pygame.Vector2(0,0)
