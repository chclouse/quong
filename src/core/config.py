from . resource_loader import *
from configparser import ConfigParser

class Config:

	PORT = 6969

	@classmethod
	def load(config):

		# config._config = ConfigParser.ConfigParser()
		# config._config.read(ResourceLoader.configuration())
		# print(config._config.get(ConfigParser.DEFAULT, 'port'))
		pass