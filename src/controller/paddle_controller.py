from . controller import *


class PaddleController(Controller):

	def __init__(self, scene, paddle):

		super(PaddleController, self).__init__(scene)

		self._paddle = paddle

		self._changed = False
		self._left    = False
		self._right   = False
		self._lastVelocity = 0


	def update(self, delta, changed = False, debug = False):

		self._changed = False
		velocity      = 0

		if self._left:
			velocity -= 500

		if self._right:
			velocity += 500

		if velocity != self._lastVelocity:
			self._changed      = True
			self._lastVelocity = velocity

		self._paddle.move(velocity)

		self._changed |= changed

		if debug:
			print(self._changed)

		return self._changed


	def rightDown(self):

		self.left  = False
		self.right = True


	def leftUp(self):

		self.left  = True
		self.right = False


	def stop(self):

		self.left  = False
		self.right = False


	@property
	def paddle(self):
		return self._paddle


	@property
	def changed(self):
		return self._changed

	@changed.setter
	def changed(self, value):
		self._changed = value


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
	