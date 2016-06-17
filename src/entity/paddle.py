from entity.entity import *
import pygame
import os


class Paddle(Entity):

	SIDE_LEFT   = 0
	SIDE_RIGHT  = 1
	SIDE_TOP    = 2
	SIDE_BOTTOM = 3

	def __init__(self, side = SIDE_LEFT):

		super(Paddle, self).__init__()

		self._side = side

		self.loadTexture()
		self.position()


	def loadTexture(self):

		directory = os.path.dirname(os.path.realpath(__file__))
		texture   = pygame.image.load(directory + "/../../res/textures/paddle.png")
		angle     = 0
		
		if self._side == Paddle.SIDE_TOP:

			angle = -90

		elif self._side == Paddle.SIDE_BOTTOM:

			angle = 90

		elif self._side == Paddle.SIDE_RIGHT:

			angle = 180
		
		self._texture = pygame.transform.rotate(texture, angle)
		self._rect    = self._texture.get_rect()


	def position(self):

		pass


	def draw(self, screen):

		super(Paddle, self).draw(screen)

		screen.blit(self._texture, self._rect)


	@property
	def side():

		return self._side
