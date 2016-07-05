import pygame


class EventManager():
	
	_cbKeyPress   = []
	_cbKeyRelease = []
	_cbQuit       = []

	@classmethod
	def onKeyPress(em, callback):

		em._cbKeyPress.append(callback)


	@classmethod
	def onKeyRelease(em, callback):

		em._cbKeyRelease.append(callback)


	@classmethod
	def onQuit(em, callback):

		em._cbQuit.append(callback)


	@classmethod
	def handleEvents(em, events):

		for event in events:

			if event.type == pygame.KEYDOWN:
				em.invoke(em._cbKeyPress, event)

			elif event.type == pygame.KEYUP:
				em.invoke(em._cbKeyRelease, event)

			elif event.type == pygame.QUIT:
				em.invoke(em._cbQuit, event)


	@classmethod
	def invoke(em, callbackList, event):

		for callback in callbackList:

			callback(event)