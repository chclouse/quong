import pickle
import socket

QUONG_PORT = 6969

class Client:


	def __init__(self, ipAddress, gameScene):

		self._ipAddress = ipAddress
		self._gameScene = gameScene

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, QUONG_PORT))
		self._socket.setblocking(False)

		self._done = False

		print("Connected")


	def send(self, key):

		self._socket.send(key.to_bytes(1, byteorder='big'))


	def receive(self):

		data = None

		try:
			data = pickle.loads(self._socket.recv(1024))

		except socket.error:
			return

		print(data)

		for i in range(0, 4):

			self._gameScene.paddles[i].x = data[i][0]
			self._gameScene.paddles[i].y = data[i][1]


	def stop(self):

		self._socket.close()
