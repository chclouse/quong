import socket

class Client:


	def __init__(self, ipAddress):

		self._ipAddress = ipAddress

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, 6969))


	def send(self, key):

		self._socket.send(key)


	def receive(self):

		pass
