import os


class ResourceLoader:

	@staticmethod
	def directory():

		return os.path.dirname(os.path.realpath(__file__))


	@staticmethod
	def sound(name):

		return ResourceLoader.directory() + '/../../res/sounds/' + name + '.wav'


	@staticmethod
	def texture(name):

		return ResourceLoader.directory() + '/../../res/textures/' + name + '.png'
