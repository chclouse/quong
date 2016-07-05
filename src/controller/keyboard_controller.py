from . paddle_controller import *
from core.event_manager import *
import pygame


class KeyboardController(PaddleController):

	KEYS_LEFT_UP    = (pygame.K_UP,   pygame.K_LEFT)
	KEYS_RIGHT_DOWN = (pygame.K_DOWN, pygame.K_RIGHT)

	def __init__(self, scene, paddle):

		super(KeyboardController, self).__init__(scene, paddle)

		EventManager.onKeyPress(self.keyEvent)
		EventManager.onKeyRelease(self.keyEvent)


	def keyEvent(self, event):

		pressed = event.type == pygame.KEYDOWN

		if event.key in KeyboardController.KEYS_LEFT_UP:
			if pressed != self.left:
				self.changed = True

			self.left = pressed

		elif event.key in KeyboardController.KEYS_RIGHT_DOWN:
			if pressed != self.right:
				self.changed = True

			self.right = pressed


	def update(self, delta):

		return super(KeyboardController, self).update(delta)
