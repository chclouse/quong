from entity.paddle import *
from scene.scene import *


class GameScene(Scene):

	def __init__(self):

		super(GameScene, self).__init__()

		self._paddle = Paddle(Paddle.SIDE_RIGHT)

		self.addEntity(self._paddle)


	def draw(self, screen):

		super(GameScene, self).draw(screen)
