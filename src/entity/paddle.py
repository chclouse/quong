from entity.entity import *
import pygame
import os


class Paddle(Entity):

	SIDE_LEFT   = 0
	SIDE_RIGHT  = 1
	SIDE_TOP    = 2
	SIDE_BOTTOM = 3

	def __init__(self, display, side = SIDE_LEFT):

		super(Paddle, self).__init__(display)

		self._side = side
		self._texture = None
		self._x = 0
		self._y = 0
		self._deltaTime = 0
		self._getTicksLastFrame = 0
		self._speed = 500

		self.loadTexture()
		self.position()



	def loadTexture(self):

		directory = os.path.dirname(os.path.realpath(__file__))
		self._texture = pygame.image.load(directory + "/../../res/textures/paddle.png")

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


	def move(self, direction):

		if self._side < 2:

			self._y = min(max(self._y + (self._speed * direction)*self._deltaTime, self.width), self._display.height - self.height - self.width)

		else:

			self._x = min(max(self.x + (self._speed * direction)*self._deltaTime, self.height), self._display.width - self.width - self.height)


	def position(self):

		if self._side < 2:

			self.y = self._texture.get_width()

		else:

			self.x = self._texture.get_height()


	def update(self):

		super(Paddle, self).update()

		t = pygame.time.get_ticks()

		#deltaTime in seconds.
		self._deltaTime = (t - self._getTicksLastFrame) / 1000.0
		self._getTicksLastFrame = t


	def draw(self, screen):

		super(Paddle, self).draw(screen)

		self._rect.left = self._x
		self._rect.top = self._y
		screen.blit(self._texture, self._rect)


	@property
	def side(self):

		return self._side


	@property
	def x(self):

		return self._x


	@x.setter
	def x(self, value):

		self._x = int(value)


	@property
	def y(self):

		return self._y


	@y.setter
	def y(self, value):

		self._y = int(value)

	@property
	def width(self):

		return self._texture.get_width()


	@property
	def height(self):
		return self._texture.get_height()
	
	
