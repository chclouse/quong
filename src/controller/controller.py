

class Controller:

	def __init__(self, scene):

		self._scene = scene


	def update(self, delta):

		pass


	@property
	def scene(self):
		return self._scene
	