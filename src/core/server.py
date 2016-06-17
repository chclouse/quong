from threading import Thread
import socket

class Server(Thread):

	def __init__(self, scene):

		super(Server, self).__init__()

		self._scene = scene

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind(('', 6969))
		self._socket.listen(4)
		self._socket.settimeout(0)
		self._socket.setblocking(False)

		self._done = False


	def send(self):

		pass


	def receive(self):

		if len(self._connections) < 4:

			while True:
				try:
					self._connections.append(self._socket.accept())
				except socket.error:
					break

		data = {}

		while True:
			try:
				for i in range(len(self._connections)):
					data[i] = self._connections[i].recv(1)
			except socket.error:
				break

		return data


	def run(self):

		while not self._done:

			self.receive()
			self.send()


	def stop(self):

		self._socket.close()
		self._done = True
