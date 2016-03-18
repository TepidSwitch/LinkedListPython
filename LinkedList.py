# Stanislav Schaller
# March 7th, 2016
# Linked List Implementation

import Node

class LinkedList:
	'''A series of nodes holding data that point in one direction to the next node in the list'''

	head = None
	tail = None

	def __init__(self, details = None):
		self.tail = Node.Node(details)

	def add(self, details = None):
		'''Adds a node and points it to the previous first node'''
		self.head = Node.Node(details)
		self.head.setNext(self.tail)
		self.tail = self.head

	def remove(self):
		'''Remove the head node and shift head and tail nodes up one'''
		self.head = self.tail
		self.tail = self.tail.getNext()

	def __str__(self):
		tmp = self.head
		output = []
		strOutput = ''

		output.append(tmp.getData())

		while(tmp.getNext()):
			maybe = tmp.getNext()
			if (maybe.getData() == None):
				output.append('None')
				print(output)
			else:
				output.append(maybe.getData())
				print(output)
			tmp = tmp.getNext()

		# Whether or not you reverse the output here is a matter of how you prefer to visualize the list getting built
		# output.reverse()

		for item in output:
			strOutput += str(item) + ' '
		return strOutput

	def cleanEmpty(self):
		'''Removes any node with a None in its data slot'''
		# Check to see if the head node is garbage. If so, remove it. Repeat. 
		# After that condition is satisfied for any head node, you can while loop

		if (self.head):
			while (self.head.getData() == None):
				self.remove()

			tmpHead = self.head
			tmpTail = self.tail

			while (tmpTail.getNext()):
				if (tmpTail.getData() == None):
					tmpTail = tmpTail.getNext()
					tmpHead.setNext(tmpTail)
				else:
					tmpHead = tmpHead.getNext()
					tmpTail = tmpTail.getNext()