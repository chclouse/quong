from threading import Thread
import socket

class Server(Thread):

	def __init__(self):

		super(Server, self).__init__()

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind(('', 6969))
		self._socket.listen(4)

		self._done = False


	def send(self):

		pass


	def receive(self):

		pass


	def run(self):

		while not self._done:

			continue


	def stop(self):

		self._socket.close()
		self._done = True
