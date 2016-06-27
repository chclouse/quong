

class Entity:

	def __init__(self, scene, display):

		self._scene   = scene
		self._display = display


	def update(self, delta):

		pass


	def draw(self, screen):

		pass


	@property
	def scene(self):
		return self._scene
	


	@property
	def display(self):
		return self._display
	
