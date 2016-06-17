import socket

QUONG_PORT = 6969

class Client:


	def __init__(self, ipAddress):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, QUONG_PORT))
		self._ipAddress = ipAddress


	def send(self, data):

		self._socket.send(data)


	def receive(self):

		pass
