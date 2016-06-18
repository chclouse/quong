from threading import Thread
import socket

class Server(Thread):

	def __init__(self, scene, controllers):

		super(Server, self).__init__()

		self._scene = scene
		self._controllers = controllers
		self._connections = []

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind(('', 6968))
		self._socket.listen(4)
		self._socket.settimeout(0)
		self._socket.setblocking(False)

		self._done = False


	def send(self):

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

		while not self._done:

			self.receive()
			self.send()

		print("Outside of the loop")


	def stop(self):

		self._done = True

		for connection in self._connections:

			connection.close()

		self._socket.close()

		print("Closing the socket")
