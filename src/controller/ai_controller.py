from . controller  import *
from entity.paddle import *


class AiController(Controller):

	def __init__(self, scene, paddle, i):

		super(AiController, self).__init__(scene)

		self._paddle = paddle
		self._i = i


	def update(self, delta):

		if self._paddle.side < 2:

			if self.scene.balls[0].y > self._paddle.y + self._paddle.height - self._paddle.width:

				self.paddle.move(500)

			elif self.scene.balls[0].y < self._paddle.y + self._paddle.width:

				self.paddle.move(-500)

		else:

			if self.scene.balls[0].x > self._paddle.x + self._paddle.width - self._paddle.height:

				self.paddle.move(500)

			elif self.scene.balls[0].x < self._paddle.x + self._paddle.height:

				self.paddle.move(-500)


	@property
	def paddle(self):
		return self._paddle
	