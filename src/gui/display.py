import pygame


class Display:


	def __init__(self, size):

		self._size = size

		self._screen = pygame.display.set_mode(size)

		self._scene = None


	def update(self):

		# Clean the display
		pygame.display.flip()

		# Draw the scene
		self._scene.draw(self._screen)


	@property
	def scene(self):	
		return self._scene


	@scene.setter
	def scene(self, scene):
		
		del self._scene
		
		self._scene = scene