from threading import Thread
import pickle
import socket

QUONG_PORT = 6968

class Client(Thread):


	def __init__(self, ipAddress, gameScene):

		super(Client, self).__init__()

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

			print("Receiving...")
			
			for i in range(0, 4):

				self._gameScene.paddles[i].x = data[i][0]
				self._gameScene.paddles[i].y = data[i][1]

		except:
			
			return None


	def run(self):

		while not self._done:

			self.receive()


	def stop(self):

		self._done = True
		self._socket.close()
