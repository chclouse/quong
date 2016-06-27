from . client import *
from . server import *
from controller.keyboard_controller import *
from gui.display import *
from scene.game_scene import *
import pygame


class Quong:

	def __init__(self, argv):

		self._argv = argv

		self._clock     = None
		self._display   = None
		self._fps       = 60
		self._lastTicks = 0
		self._size      = (600, 600)

		self._finished = False
		self._exitCode = 0

		pygame.mixer.init()


	def initialize(self):

		pygame.init()

		self._clock   = pygame.time.Clock()
		self._display = Display(self._size)

		self._scene = GameScene(self._display)


	def run(self):

		self.initialize()

		while not self._finished:

			events = pygame.event.get()

			for event in events:

				if event.type == pygame.QUIT:

					self.exit(0)

			ticks = pygame.time.get_ticks()

			#deltaTime in seconds.
			delta = (ticks - self._lastTicks) / 1000.0
			self._lastTicks = ticks

			self._scene.update(events, delta)
			self._scene.draw(self._display.screen)
			self._display.update()

			self._clock.tick(self._fps)

		self._scene.close()

		return self._exitCode


	def exit(self, exitCode):

		self._finished = True
		self._exitCode = exitCode
