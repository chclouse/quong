from entity.paddle import *
from scene.scene import *


class GameScene(Scene):

	def __init__(self, display):

		super(GameScene, self).__init__(display)

		self._paddle = Paddle(display, Paddle.SIDE_LEFT)

		self.addEntity(self._paddle)


	def draw(self, screen):

		screen.fill((0, 0, 0))

		super(GameScene, self).draw(screen)
