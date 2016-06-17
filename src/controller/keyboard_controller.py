<<<<<<< HEAD
from . controller import *
=======
from controller.controller import *
import pygame
>>>>>>> 4f9d2877b61cc4df0ad25bbe3c9b541f858a2a99


class KeyboardController(Controller):

	def __init__(self, connection):

		self._connection = connection


	def update(self, update):

		keyPressed = 0x4 if update.type == pygame.KEYDOWN else 0x0
		keyDownRight = 0x2 if update.key in (pygame.K_DOWN, pygame.K_RIGHT) else 0x0
		keyLeftUp = 0x1 if update.key in (pygame.K_UP, pygame.K_LEFT) else 0x0

		self._connection.send((keyPressed | keyDownRight | keyLeftUp).to_bytes(1, byteorder='big'))

