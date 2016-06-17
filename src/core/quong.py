from . client import *
from . server import *
from controller.keyboard_controller import *
from gui.display import *
from scene.game_scene import *
import pygame


class Quong:

	def __init__(self, argv):

		self._argv = argv

		self._clock   = None
		self._display = None
		self._fps     = 60
		self._size    = (600, 600)

		self._finished = False
		self._exitCode = 0


	def initialize(self):

		pygame.init()

		self._clock   = pygame.time.Clock()
		self._display = Display(self._size)

		self._scene      = GameScene(self._display)
		self._controller = KeyboardController()


	def connect(self):

		if len(self._argv) == 1:

			self._server = Server()
			self._server.start()

			self._conneciton = Client('127.0.0.1')

		else:

			self._connection = Client(self._argv[1])


	def run(self):

		self.initialize()

		self.connect()

		while not self._finished:

			for event in pygame.event.get():

				if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:

					self._controller.update(event)

				if event.type == pygame.QUIT:

					self.exit(0)

			# Update the scene
			self._scene.update()

			# Draw the scene
			self._scene.draw(self._display.screen)

			self._display.update()

			# Wait until next frame
			self._clock.tick(self._fps)

		self._server.stop()
		self._server.join()

		return self._exitCode


	def exit(self, exitCode):

		self._finished = True
		self._exitCode = exitCode
