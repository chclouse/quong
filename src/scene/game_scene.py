from controller.keyboard_controller import *
from controller.network_controller  import *
from core.server   import *
from entity.paddle import *
from scene.scene   import *
import sys


class GameScene(Scene):

	def __init__(self, display):

		super(GameScene, self).__init__(display)

		self._connection  = None
		self._controllers = []
		self._paddles     = []

		self.initPaddles()

		self.connect()



	def connect(self):

		if len(sys.argv) == 1:

			self._server = Server(self, self._paddles)
			self._server.start()

			self._connection = Client('127.0.0.1')

		else:

			self._connection = Client(sys.argv[1])


	def initPaddles(self):

		for i in range(0, 4):

			paddle = Paddle(self._display, i)
			controller = NetworkController(paddle)

			self._paddles.append(paddle)
			self._controllers.append(controller)

			self.addEntity(self._paddle)


		self._controller = KeyboardController(self._connection)


	def update(self):

		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:

				self._controller.update(event)


	def draw(self, screen):

		screen.fill((0, 0, 0))

		super(GameScene, self).draw(screen)
