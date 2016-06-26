

class Entity:

	def __init__(self, display):

		self._display = display


	def update(self, delta):

		pass


	def draw(self, screen):

		pass


	@property
	def display(self):
		return self._display
	
