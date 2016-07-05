from . client        import *
from . event_manager import *
from . server        import *
from controller.keyboard_controller import *
from gui.display      import *
from scene.game_scene import *
import pygame
import time

_instance = None

class Quong:

	@staticmethod
	def instance(self):

		global _instance
		return _instance


	def __init__(self, argv):
		
		global _instance

		self._argv = argv

		self._clock     = None
		self._display   = None
		self._fps       = 60
		self._lastTicks = 0
		self._size      = (600, 600)

		self._finished = False
		self._exitCode = 0

		pygame.mixer.init()

		_instance = self


	def initialize(self):

		pygame.init()

		EventManager.onQuit(self.exit)

		self._clock   = pygame.time.Clock()
		self._display = Display(self._size)

		self._scene = GameScene(self._display)


	def run(self):

		self.initialize()

		while not self._finished:

			# Events are handled before the update or draw methods are invoked
			EventManager.handleEvents(pygame.event.get())

			ticks = pygame.time.get_ticks()

			#deltaTime in seconds.
			delta = (ticks - self._lastTicks) / 1000.0
			self._lastTicks = ticks
			
			self._scene.update(delta)
			self._scene.draw(self._display.screen)
			self._display.update()

			self._clock.tick(self._fps)

		self._scene.close()

		return self._exitCode


	def exit(self, exitCode = 0):

		self._finished = True
		self._exitCode = exitCode


	def onKeyPress(self, callback):

		self._cbKeyPress.append(callback)


	def onKeyRelease(self, callback):

		self._cbKeyRelease.append(callback)


	@property
	def events(self):
		return self._events
	
