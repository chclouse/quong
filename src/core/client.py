import pickle
import socket
import struct

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

		buf       = b''
		data      = None
		positions = None

		# Add all pending data to the buffer
		while True:
			try:
				buf += self._socket.recv(1024)

			except socket.error:
				break

		# Loop through and discard all old buffer data
		while len(buf):

			try:
				length = struct.unpack('!H', buf[0:2])[0]
				data   = buf[2:length + 2]

				buf = buf[length + 2:]

				positions = pickle.loads(data)

			except EOFError:
				pass

		if positions:

			for i in range(0, 4):

				self._gameScene.paddles[i].x = positions[0][i][0]
				self._gameScene.paddles[i].y = positions[0][i][1]

			if not self._gameScene.isHost:

				for i in range(len(positions[1])):

					self._gameScene.balls[i].x = positions[1][i][0]
					self._gameScene.balls[i].y = positions[1][i][1]

	def stop(self):

		self._socket.close()

		print("Socket closed")
