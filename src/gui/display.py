import pygame


class Display:


	def __init__(self, size):

		self._size = size

		self._screen = pygame.display.set_mode(size)

		self._scene = None


	def clean(self):
		
		pygame.display.flip()


	@property
	def scene(self):	
		return self._scene


	@scene.setter
	def scene(self, scene):
		
		del self._scene

		self._scene = scene


	@property
	def screen(self):

		return self._screen