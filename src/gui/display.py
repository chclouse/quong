import pygame


class Display:


	def __init__(self, size):

		self._size = size

		self._screen = pygame.display.set_mode(size)


	def update(self):

		pygame.display.flip()