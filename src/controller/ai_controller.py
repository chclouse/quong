from . paddle_controller import *
from entity.paddle       import *


class AiController(PaddleController):

	def __init__(self, scene, paddle, identifier):

		super(AiController, self).__init__(scene, paddle)

		self._paddle     = paddle
		self._identifier = identifier # AI identifier


	def update(self, delta):

		if self._identifier != 1:

			return False

		self.changed = False

		if self._paddle.side < 2:

			if self.scene.balls[0].y > self._paddle.y + self._paddle.height - self._paddle.width:
				self.rightDown()

			elif self.scene.balls[0].y < self._paddle.y + self._paddle.width:
				self.leftUp()

			else:
				self.stop()

		else:

			if self.scene.balls[0].x > self._paddle.x + self._paddle.width - self._paddle.height:
				self.rightDown()

			elif self.scene.balls[0].x < self._paddle.x + self._paddle.height:
				self.leftUp()

			else:
				self.stop()

		return super(AiController, self).update(delta, self.changed, self._identifier == 1)
	