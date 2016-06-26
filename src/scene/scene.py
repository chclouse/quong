

class Scene:

	def __init__(self, display):

		self._entities = []

		self._display = display


	def addEntity(self, entity):

		self._entities.append(entity)


	def update(self, events, delta):

		for entity in self._entities:

			entity.update(delta)


	def draw(self, screen):

		for entity in self._entities:

			entity.draw(screen)


	def close(self):

		pass


	@property
	def display(self):
		return self._display
	
