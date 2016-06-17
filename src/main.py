#!/usr/bin/python3

from core.quong import *
import sys


def main(argv):
	
	app = Quong(argv)

	sys.exit(app.run())


if __name__ == "__main__":
	main(sys.argv)
