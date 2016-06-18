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
		self._x = 0
		self._y = 0
		self._deltaTime = 0

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


	def move(self, direction):

		if self._side < 2:

			self._y = min(max(self._y + (50 * direction)*self._deltaTime, 0), self._display.height - self._texture.get_height() - self._texture.get_width())

		else:

			self._x = min(max(self.x + (50 * direction)*self._deltaTime, 0), self._display.width - self._texture.get_width() - self._texture.get_height())


	def position(self):

		if self._side < 2:

			self.y = self._texture.get_width()

		else:

			self.x = self._texture.get_height()


	def update(self):

		super(Paddle, self).update()

		t = pygame.time.get_ticks()
		#deltaTime in seconds.
		self._deltaTime = (t - getTicksLastFrame) / 1000.0
		getTicksLastFrame = t


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

		self._x = value


	@property
	def y(self):

		return self._y


	@y.setter
	def y(self, value):

		self._y = value
