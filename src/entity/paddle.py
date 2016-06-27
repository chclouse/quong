from core.resource_loader import *
from entity.entity        import *
import math
import os
import pygame


class Paddle(Entity):

	SIDE_LEFT   = 0
	SIDE_RIGHT  = 1
	SIDE_TOP    = 2
	SIDE_BOTTOM = 3

	SPEED_MAX =  1000
	SPEED_MIN = -SPEED_MAX

	def __init__(self, scene, display, side = SIDE_LEFT):

		super(Paddle, self).__init__(scene, display)

		self._side = side
		self._texture = None
		self._x = 0
		self._y = 0
		self._speed = 0
		self._acceleration = 0.2

		self._dx = 0
		self._dy = 0

		self.loadTexture()
		self.position()



	def loadTexture(self):

		self._texture = pygame.image.load(ResourceLoader.texture('paddle'))

		if self._side == Paddle.SIDE_LEFT:

			angle = 0

		elif self._side == Paddle.SIDE_TOP:

			angle = -90

		elif self._side == Paddle.SIDE_BOTTOM:

			angle = 90
			self._y = self.display.height - self.width

		else:

			angle = 180
			self._x = self.display.width - self.width

		self._texture = pygame.transform.rotate(self._texture, angle)
		self._rect    = self._texture.get_rect()


	def move(self, speed):

		self._speed = min(max(self._speed + speed * self._acceleration, Paddle.SPEED_MIN), Paddle.SPEED_MAX)

		#print(self._speed)


	def position(self):

		if self._side < 2:

			self.y = self._texture.get_width()

		else:

			self.x = self._texture.get_height()


	def update(self, delta):

		super(Paddle, self).update(delta)

		self._dx = 0
		self._dy = 0

		if self._side < 2:

			self.y += self._speed*delta
			if self._speed != 0:
				self._dy = self._speed

		else:

			self.x += self._speed*delta
			if self._speed != 0:
				self._dx = self._speed

		self._speed -= self._speed * self._acceleration
		#self._speed *= self._acceleration
		#print("-" + str(self._speed))


	def draw(self, screen):

		super(Paddle, self).draw(screen)

		self._rect.left = self._x
		self._rect.top = self._y
		screen.blit(self._texture, self._rect)


	def getNormal(self):

		if self._side == Paddle.SIDE_LEFT:

			return 0

		elif self._side == Paddle.SIDE_BOTTOM:

			return 0.5*math.pi

		elif self._side == Paddle.SIDE_RIGHT:

			return math.pi

		elif self._side == Paddle.SIDE_TOP:

			return 1.5*math.pi

		else:

			return None


	@property
	def side(self):

		return self._side


	@property
	def x(self):

		return self._x


	@x.setter
	def x(self, value):

		if self.side < 2:

			self._x = 0 if self.side == 0 else self._display.width - self.width

		else:

			self._x = min(max(value, self.height), self._display.width - self.width - self.height)


	@property
	def y(self):

		return self._y


	@y.setter
	def y(self, value):

		if self.side < 2:

			self._y = min(max(value, self.width), self._display.height - self.width - self.height)

		else:

			self._y = 0 if self.side == 2 else self._display.height - self.height

	@property
	def width(self):

		return self._texture.get_width()


	@property
	def height(self):
		return self._texture.get_height()


	@property
	def rect(self):
		return self._rect
