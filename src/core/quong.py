from gui.display import *
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


	def run(self):

		if not pygame.init():

			return 1

		self._clock   = pygame.time.Clock()
		self._display = Display(self._size)

		while not self._finished:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					self._finished = True

			# Refresh the screen
			self._display.update()

			# Make the game run at the given fps
			self._clock.tick(self._fps)


		return self._exitCode