import socket
<<<<<<< HEAD
=======

QUONG_PORT = 6969
>>>>>>> 4f9d2877b61cc4df0ad25bbe3c9b541f858a2a99

class Client:


	def __init__(self, ipAddress):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, QUONG_PORT))
		self._ipAddress = ipAddress

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, 6969))

<<<<<<< HEAD

	def send(self, key):

		self._socket.send(key)
=======
	def send(self, data):

		self._socket.send(data)
>>>>>>> 4f9d2877b61cc4df0ad25bbe3c9b541f858a2a99


	def receive(self):

		pass
