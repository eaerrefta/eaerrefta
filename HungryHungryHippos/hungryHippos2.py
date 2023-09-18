import pygame
import random
import eatingwatermelon
import foodwatermelon
import hippo
from pygame.locals import *


def makeFood():
	newFood = foodwatermelon.FoodWatermelon(screen, 6, 5)
	return newFood


pygame.init()

size = height, width = 1000, 900

screen = pygame.display.set_mode(size)

player = pygame.Rect((size[0]/2, size[1]/2, 50,50))

text_font = pygame.font.SysFont("Arial", 30, italic=True)
#text_font = pygame.font.SysFont(None, 30, bold=True, italic=True)


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

score = 0

GREEN = (0,255,0)
PINK = (200, 50, 50)
BLUE = (0,0,255)

player = hippo.Hippo(screen, 6)

player_group = pygame.sprite.Group()
player_group.add(player)

watermelon_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

clock = pygame.time.Clock()


paused = False
running = True
while running:
	clock.tick(60)

	screen.fill((50,50,50))

	scoreText = "Score: " + str(score)

	draw_text(scoreText, text_font, BLUE, 0,0)

	key = pygame.key.get_pressed()


	if not paused:
		if key[pygame.K_a] == True:
			player.vectorUpdate((-3, 0))
		if key[pygame.K_d] == True:
			player.vectorUpdate((3, 0))
		if key[pygame.K_w] == True:
			player.vectorUpdate((0, -3))
		if key[pygame.K_s] == True:
			player.vectorUpdate((0, 3))
		player_group.update()
		player_group.draw(screen)
		watermelon_group.draw(screen)
		food_group.draw(screen)
		watermelon_group.update()
		food_group.update()

	if paused:
		draw_text("Game Paused.", text_font, BLUE, 2*size[0]/5,size[1]/2-50)
		draw_text("Press r to resume.", text_font, BLUE, 2*size[0]/5,size[1]/2+0)
		draw_text("Press q to quit.", text_font, BLUE, 2*size[0]/5,size[1]/2+50)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				paused = True
			if event.key == pygame.K_r:
				paused = False
			if event.key == pygame.K_q:
				running = False

	if len(food_group)<10:
		newFood = makeFood()
		food_group.add(newFood)

	for food in food_group:
		if food.rect.colliderect(player.rect):
			if pygame.sprite.spritecollide(food, player_group, False, pygame.sprite.collide_mask):
				pos = food.rect.center
				melonEat = eatingwatermelon.EatingWatermelon(pos[0],pos[1], scale=6, rotationAngle=food.rotationAngle)
				watermelon_group.add(melonEat)
				food_group.remove(food)
				score += 1


	pygame.display.flip()

pygame.quit()