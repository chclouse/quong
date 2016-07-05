from . config import *
import pickle
import socket
import struct
import time


class Client:


	def __init__(self, host, scene):

		self._host   = host
		self._scene  = scene
		self._id     = -1
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.connect()

		print("Connected")


	def connect(self):

		port = Config.PORT
		while True:
			try:
				self._socket.connect((self._host, port)) # Temporary try that finds moved port
				break
			except:
				port -= 1

		self._id = pickle.loads(self._socket.recv(1024))[0]
		self._socket.setblocking(False)


	def send(self, controller):

		self._socket.send(
			pickle.dumps(
				(controller.left, controller.right)
			)
		)


	def receive(self):

		buffer = b''
		data   = None
		
		# Add all pending data to the buffer
		while True:
			try:
				buffer += self._socket.recv(1024)
			except socket.error:
				break

			except Exception as e:
				print(e)
				break

		# Loop through and discard all old buffer data
		while len(buffer):

			try:
				length = struct.unpack('!H', buffer[0:2])[0]
				packet = buffer[2:length + 2]

				buffer = buffer[length + 2:]

				data = pickle.loads(packet)

			except EOFError as e:
				print(e)

		if data:

			self.updateScene(data)

			#if not self._scene.isHost:

			#	for i in range(len(positions[1])):

			#		self._scene.balls[i].x = positions[1][i][0]
			#		self._scene.balls[i].y = positions[1][i][1]
		
		return data
					
					
	def updateScene(self, data):

		for i in range(0, 4):

			controller = self._scene.controllers[i]

			controller.left     = data[1][i][0]
			controller.right    = data[1][i][1]
			controller.paddle.x = data[1][i][2]
			controller.paddle.y = data[1][i][3]


	def stop(self):

		print("Closing...")
		self._socket.close()
		print("Socket closed")


	@property
	def id(self):
		return self._id
	
