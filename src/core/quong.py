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

		self._scene = GameScene(self._display)


	def run(self):

		self.initialize()

		while not self._finished:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					self.exit(0)

			# Update the scene
			self._scene.update()

			# Draw the scene
			self._scene.draw(self._display.screen)

			# Wait until next frame
			self._clock.tick(self._fps)


		return self._exitCode


	def exit(self, exitCode):

		self._finished = True
		self._exitCode = exitCode
