import pygame
from pygame.locals import *
import spritesheet
import random

#EatingWatermelon class
class FoodWatermelon(pygame.sprite.Sprite):
	def __init__(self, surf, scale=1, speedInput=1):
		pygame.sprite.Sprite.__init__(self)
		sprite_sheet_image = pygame.image.load("images/watermelon.png").convert_alpha()
		sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
		self.masterImage = sprite_sheet.get_image(0, 24, 24, scale, (0,0,0))
		self.image = self.masterImage
		self.rect = self.image.get_rect()

		self.imgOffset = 24*scale
		self.surfSize = surf.get_size() #(width, height)
		self.startPos = (-1*self.imgOffset, random.randint(0, self.surfSize[1]-self.imgOffset))
		self.endPos = (self.surfSize[0]+self.imgOffset, random.randint(0, self.surfSize[1]-self.imgOffset))

		self.directionVector = pygame.Vector2((self.endPos[0]-self.startPos[0]),(self.endPos[1]-self.startPos[1]))
		self.unitVector = self.directionVector.normalize()

		self.rect.center = self.startPos

		self.rotationAngle = 0
		self.speed = speedInput
		self.counter = 0
		self.speedVector = self.unitVector*self.speed
		self.curPos = self.startPos

		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		if self.counter == 4:
			if self.rotationAngle < 360:
				self.rotationAngle += 10
				self.image = pygame.transform.rotate(self.masterImage, self.rotationAngle).convert_alpha()
				self.rect = self.image.get_rect()
				self.mask = pygame.mask.from_surface(self.image)
				self.counter = 0
			else:
				self.rotationAngle = 0
				self.image = pygame.transform.rotate(self.masterImage, self.rotationAngle).convert_alpha()
				self.rect = self.image.get_rect()
				self.mask = pygame.mask.from_surface(self.image)
				self.counter = 0
		else:
			self.counter += 1

		if self.curPos[0]<self.surfSize[0]+self.imgOffset:
			self.curPos += self.speedVector
			self.rect.center = self.curPos
		else:
			self.curPos = self.startPos
			self.rect.center = self.curPos