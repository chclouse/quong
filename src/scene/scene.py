

class Scene:

	def __init__(self):

		self._entities = []


	def addEntity(self, entity):

		self._entities.append(entity)


	def draw(self, screen):

		for entity in self._entities:

			entity.draw(screen)
