import pickle
import socket

class Server:

	def __init__(self, scene, controllers):

		self._scene = scene
		self._controllers = controllers
		self._connections = []

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind(('', 6969))
		self._socket.listen(4)
		self._socket.settimeout(0)
		self._socket.setblocking(False)

		self._done = False


	def send(self):

		# Create a list of all of the paddle's positions
		positions = [(controller.paddle.x, controller.paddle.y) for controller in self._controllers]

		for i in range(1, len(self._connections)):

			try:
				self._connections[i].send(pickle.dumps(positions))
			except:
				pass


	def receive(self):

		if len(self._connections) < 4:

			try:
				connection, address = self._socket.accept()

				connection.setblocking(False)

				self._connections.append(connection)

			except:
				pass

		for i in range(len(self._connections)):


			try:
				data = int.from_bytes(self._connections[i].recv(1), byteorder='big')

				if data & 0x1:

					self._controllers[i].left = data & 0x4

				else:

					self._controllers[i].right = data & 0x4

			except Exception as e:
				continue


	def run(self):

		self.receive()
		self.send()


	def stop(self):

		for connection in self._connections:

			connection.close()

		self._socket.close()

		print("Closing the socket")
