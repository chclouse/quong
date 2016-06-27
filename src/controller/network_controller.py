from . controller import *


class NetworkController(Controller):

	def __init__(self, scene, paddle):

		super(NetworkController, self).__init__(scene)

		self._paddle = paddle

		self._left  = False
		self._right = False


	def update(self, delta):

		if self._left:

			self._paddle.move(-1)

		elif self._right:

			self._paddle.move(1)


	@property
	def paddle(self):
		return self._paddle
	


	@property
	def left(self):
		return self._left

	@left.setter
	def left(self, value):
		self._left = value


	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, value):
		self._right = value
	