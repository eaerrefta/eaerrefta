import pygame
from pygame.locals import *
import spritesheet

#EatingWatermelon class
class EatingWatermelon(pygame.sprite.Sprite):
	def __init__(self, x, y, scale=1, rotationAngle=0):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		sprite_sheet_image = pygame.image.load("images/watermelonEating.png").convert_alpha()
		sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
		for place in range(4):
			tempImg = sprite_sheet.get_image(place, 24, 24, scale, (0,0,0))
			tempImg = pygame.transform.rotate(tempImg, rotationAngle).convert_alpha()
			self.images.append(tempImg)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		animation_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= animation_speed and self.index < len(self.images)-1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images)-1 and self.counter >= animation_speed:
			self.kill()