from entity.entity import *


class Paddle(Entity):

	SIDE_LEFT   = 0
	SIDE_RIGHT  = 1
	SIDE_TOP    = 2
	SIDE_BOTTOM = 3

	def __init__(self, side = Paddle.SIDE_LEFT):

		super(Paddle, self).__init__()

		self._side = side


	def draw(self):

		super(Paddle, self).draw()


	@property
	def side():

		return self._side