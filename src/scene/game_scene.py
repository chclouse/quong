from controller.keyboard_controller import *
from controller.network_controller  import *
from core.client   import *
from core.server   import *
from entity.paddle import *
from scene.scene   import *
import sys


class GameScene(Scene):

	def __init__(self, display):

		super(GameScene, self).__init__(display)

		self._host = False
		self._connection  = None
		self._controllers = []
		self._paddles     = []
		self._balls = []

		self.initPaddles()

		self.connect()

		self._controller = KeyboardController(self._connection)



	def connect(self):

		print(sys.argv)

		if len(sys.argv) == 1:

			self._host = True

			self._server = Server(self, self._controllers)
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

			self.addEntity(paddle)

	def initBall(self):

		ball = Ball(self._display, self._paddles)

		self._balls.append(ball)

		self.addEntity(ball)


	def update(self, events):

		super(GameScene, self).update(events)

		for event in events:

			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:

				self._controller.update(event)

		for controller in self._controllers:

			controller.update()

		if not self._host:

			data = self._client.receive()

			if data:

				for i in range(0, 4):

					self._paddles[i].x = data[i][0]
					self._paddles[i].y = data[i][1]


	def draw(self, screen):

		screen.fill((0, 0, 0))

		super(GameScene, self).draw(screen)


	def close(self):

		self._server.stop()
		self._server.join()
