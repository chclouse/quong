from . controller import *
import pygame


class KeyboardController(Controller):

	def __init__(self, connection):

		self._connection = connection


	def update(self, update):

		keyPressed = 0x4 if update.type == pygame.KEYDOWN else 0x0
		keyDownRight = 0x2 if update.key in (pygame.K_DOWN, pygame.K_RIGHT) else 0x0
		keyLeftUp = 0x1 if update.key in (pygame.K_UP, pygame.K_LEFT) else 0x0

		self._connection.send(keyPressed | keyDownRight | keyLeftUp)

		print("Key press")