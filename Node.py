# Stanislav Schaller
# March 7th, 2016
# 2D Node 

class Node:
	'''Basic 1D Node'''

	def __init__(self, details = None, overThere = None):
		self.data = details
		self.nextNode = overThere

	def setData(self, details):
		'''Set the data slot'''
		self.data = details

	def getData(self):
		'''Get the stuff in the data slot'''
		return self.data

	def setNext(self, overThere):
		'''Set where this node points to'''
		self.nextNode = overThere

	def getNext(self):
		'''Return the node that this one points to'''
		return self.nextNode

	def __str__(self):
		return str(self.data)