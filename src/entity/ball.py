from entity.entity import *
import math
import os
import pygame
import random


class Ball(Entity):

	def __init__(self, display, paddles):

		super(Ball, self).__init__(display)

		self._speed          = 100
		self._lastFrameTicks = pygame.time.get_ticks()
		self._trajectory     = random.randint(0, 3) * 0.5 * math.pi

		self.loadTexture()
		self._x, self._y = display.width/2 - self._size[0], display.height/2 - self._size[1]


	def loadTexture(self):

		directory = os.path.dirname(os.path.realpath(__file__))
		self._texture =  pygame.image.load(directory + "/../../res/textures/ball.png")
		self._rect    =  self._texture.get_rect()
		self._size    =  self._texture.get_size()


	def update(self):

		super(Ball, self).update()

		t = pygame.time.get_ticks()
		deltaTime = (t - self._lastFrameTicks) / 1000.0
		self._lastFrameTicks = t

		self._x = self._x + math.cos(self._trajectory)*deltaTime*self._speed
		self._y = self._y + math.sin(self._trajectory)*deltaTime*self._speed


	def draw(self, screen):

		super(Ball, self).draw(screen)

		self._rect.left = self._x
		self._rect.top = self._y
		screen.blit(self._texture, self._rect)
