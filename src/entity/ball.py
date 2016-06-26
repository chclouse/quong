from entity.entity import *
import os
import pygame
import random


class Ball(Entity):

	def __init__(self, display, paddles):

		super(Ball, self).__init__(display)

		self.loadTexture()
		self._x, self._y = display.width/2 - self._size[0], display.height/2 - self._size[1]
		self._trajectory = random.choice((-1, 1)), random.choice((-1, 1))
		self._rect.move_ip(self._x, self._y)


	def loadTexture(self):

		directory = os.path.dirname(os.path.realpath(__file__))
		self._texture =  pygame.image.load(directory + "/../../res/textures/ball.png")
		self._rect    =  self._texture.get_rect()
		self._size    =  self._texture.get_size()


	def update(self):

		super(Ball, self).update()


	def draw(self, screen):

		super(Ball, self).draw(screen)

		screen.blit(self._texture, self._rect)
