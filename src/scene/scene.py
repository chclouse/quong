

class Scene:

	def __init__(self, display):

		self._entities = []

		self._display = display


	def addEntity(self, entity):

		self._entities.append(entity)


	def update(self):

		for entity in self._entities:

			entity.update()


	def draw(self, screen):

		

		for entity in self._entities:

			entity.draw(screen)
