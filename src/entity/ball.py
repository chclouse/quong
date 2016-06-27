from core.resource_loader import *
from entity.entity        import *
import math
import pygame
import random


class Ball(Entity):

	def __init__(self, scene, display, paddles):

		super(Ball, self).__init__(scene, display)

		self._speed          = 100
		self._lastFrameTicks = pygame.time.get_ticks()
		self._trajectory     = math.pi   # Change to random direction later.
		self._paddles        = paddles

		self._collideSound   = pygame.mixer.Sound(ResourceLoader.sound('paddle_hit'))
		self._lastPaddle     = None

		self.loadTexture()
		self._x, self._y = (display.width/2 - self._size[0],
		                    display.height/2 - self._size[1])


	def loadTexture(self):

		self._texture =  pygame.image.load(ResourceLoader.texture('ball'))
		self._rect    =  self._texture.get_rect()
		self._size    =  self._texture.get_size()


	def serve(self):

		self._x = self._display.width/2
		self._y = self._display.height/2

		self._trajectory = math.pi


	def update(self, delta):

		super(Ball, self).update(delta)

		if not self.scene.isHost:

			self._rect.left = self._x
			self._rect.top = self._y

			return

		self._x = self._x + math.cos(self._trajectory)*delta*self._speed
		self._y = self._y + math.sin(self._trajectory)*delta*self._speed
		self._rect.left = self._x
		self._rect.top = self._y

		collidingPaddle = self.getCollidingPaddle()

		if collidingPaddle != None:

			alterTraj = collidingPaddle._speed

			#print(collidingPaddle._speed)

			self._trajectory += (math.pi+alterTraj)


	def draw(self, screen):

		super(Ball, self).draw(screen)

		screen.blit(self._texture, self._rect)


	def getCollidingPaddle(self):

		paddleRects = [p.rect for p in self._paddles]
		collision = self._rect.collidelist(paddleRects)

		if collision == -1:

			return None

		else:


			return self._paddles[collision]


	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, value):
		self._speed = value


	@property
	def trajectory(self):
		return self._trajectory

	@trajectory.setter
	def trajectory(self, value):
		self._trajectory = value


	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value


	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		self._y = value
