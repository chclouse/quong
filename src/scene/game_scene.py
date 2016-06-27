from controller.ai_controller import *
from controller.keyboard_controller import *
from controller.network_controller  import *
from core.client   import *
from core.server   import *
from entity.ball   import *
from entity.paddle import *
from scene.scene   import *
import sys


class GameScene(Scene):

	def __init__(self, display):

		super(GameScene, self).__init__(display)

		self._host = False
		self._controllers = []
		self._paddles     = []
		self._balls       = []

		self._connection  = None

		self.initPaddles()
		self.initBall()

		self.connect()

		self._controller = KeyboardController(self, self._connection)


	def connect(self):

		print(sys.argv)

		if len(sys.argv) == 1:

			self._host = True

			self._server = Server(self)

			self._connection = Client('127.0.0.1', self)

		else:

			self._connection = Client(sys.argv[1], self)


	def initPaddles(self):

		for i in range(0, 4):

			paddle = Paddle(self._display, i)

			self._paddles.append(paddle)
			self._controllers.append(AiController(self, paddle, i))

			self.addEntity(paddle)


	def initBall(self):

		ball = Ball(self._display, self._paddles)

		self._balls.append(ball)

		self.addEntity(ball)


	def update(self, events, delta):

		super(GameScene, self).update(events, delta)

		for event in events:

			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:

				self._controller.update(event, delta)

		for controller in self._controllers:

			controller.update(delta)

		if self._host:

			self._server.run()

		self._connection.receive()


	def draw(self, screen):

		screen.fill((0, 0, 0))

		super(GameScene, self).draw(screen)


	def close(self):

		print("Closing")

		self._connection.stop()

		if self._host:

			self._server.stop()


	@property
	def balls(self):
		return self._balls
	


	@property
	def controllers(self):
		return self._controllers
	

	@property
	def paddles(self):
		return self._paddles
	
