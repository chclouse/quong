from . config import *
from controller.paddle_controller import *
from threading import Thread
import pickle
import socket
import struct

class Server(Thread):

	def __init__(self, scene):

		super(Server, self).__init__()

		self._scene = scene
		self._connections = []

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		port = Config.PORT
		while True:
			try:
				self._socket.bind(('', port)) # Temporary try that binds to unused port
				break
			except:
				port -= 1
		self._socket.listen(4)
		self._socket.settimeout(0)
		self._socket.setblocking(False)

		self._received = False
		self._done     = False


	def send(self):

		for i in range(len(self._connections)):
			
			try:
				data   = pickle.dumps([i] + self.getSceneData())
				packet = struct.pack('!H', len(data)) + data
				
				self._connections[i].sendall(packet)
				

			except socket.error as e:
				print('Server Send Error', e)

		self._received = False


	def receive(self):

		if len(self._connections) < 4:

			try:
				connection, address = self._socket.accept()
				print("Connection established", connection)

				index = len(self._connections)

				self._scene.controllers[index] = PaddleController(self._scene, self._scene.paddles[index])
				self._connections.append(connection)
				connection.setblocking(False)

				connection.sendall(pickle.dumps((index,)))

			except Exception as e:
				pass

		for i in range(len(self._connections)):

			controller = self._scene.controllers[i]

			try:
				data = pickle.loads(self._connections[i].recv(8))

				controller.left  = data[0]
				controller.right = data[1]

				print(data)

				self._received = True

			except Exception as e:
				continue

		return self._received


	def run(self):

		while not self._done:

			self.receive()


	def stop(self):

		self._done = True

		for connection in self._connections:

			connection.close()

		self._socket.close()

		print("Closing the socket")


	def getSceneData(self):

		# Create a list of all of the paddle's positions
		positions = []
		positions.append(
			[(
				controller.left,     controller.right,
				controller.paddle.x, controller.paddle.y
			 )
			for controller in self._scene.controllers]
		)

		return positions


	@property
	def received(self):
		return self._received
	