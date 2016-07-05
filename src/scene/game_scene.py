from controller.ai_controller import *
from controller.keyboard_controller import *
from controller.paddle_controller  import *
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
		self._controller  = None
		self._controllers = []
		self._paddles     = []
		self._balls       = []

		self._connection  = None

		self.initPaddles()
		self.initBall()

		self.connect()

		self._balls[0].serve()


	def initPaddles(self):

		for i in range(0, 4):

			paddle = Paddle(self, self._display, i)

			self._paddles.append(paddle)

			self.addEntity(paddle)


	def initBall(self):

		ball = Ball(self, self._display, self._paddles)

		self._balls.append(ball)

		self.addEntity(ball)


	def connect(self):
		
		if len(sys.argv) == 1:

			self._host   = True
			self._server = Server(self)
			self._server.start()

			for i in range(0, 4):
				self._controllers.append(AiController(self, self._paddles[i], i))

		else:

			for i in range(0, 4):
				self._controllers.append(PaddleController(self, self._paddles[i]))
		print("Connecting...")
		self._connection = Client('127.0.0.1' if self._host else sys.argv[1], self)
		self._controller = KeyboardController(self, self._paddles[self._connection.id])
		self._controllers[self._connection.id] = self._controller

		print(self._controllers[self._connection.id] == self._controller)


	def update(self, delta):

		super(GameScene, self).update(delta)

		changed = False

		self._connection.receive()

		for controller in self._controllers:
			changed |= controller.update(delta)

		if self._controller.changed:
			self._connection.send(self._controller)

		if self._host and (changed or self._server.received):
			self._server.send()


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
	def isHost(self):
		return self._host
	

	@property
	def paddles(self):
		return self._paddles
