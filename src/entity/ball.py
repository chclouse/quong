from entity.entity import *


class Ball(Entity):

	def __init__(self, display, paddles):

		super(Ball, self).__init__(display)

		self.loadTexture()

	def loadTexture(self):
		directory = os.path.dirname(os.path.realpath(__file__))
		texture   = pygame.image.load(directory + "/../../res/textures/ball.png")

		self._texture =  texture
		self._rect    =  self._texture.get_rect()


	def update(self):

		super(Ball, self).update()


	def draw(self, screen):

		super(Ball, self).draw(screen)

		screen.blit(self._texture, self._rect)
