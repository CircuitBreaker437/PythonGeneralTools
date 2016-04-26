# Filename: double_linked_list.py
# Programmer: Marcin Czajkowski
<<<<<<< HEAD
# Revision: 4.0 - Final working version - fixed references to nodes in linked list 
#                 in removeNode() method
=======
# Revision: 3.0 - Syntax fixed - line 50 missing ':'
>>>>>>> e4fbe07ded490fececa1b4736a74fa0387a39efa
# Purpose: The purpose of this script is to create a doubly linked list example.
#          The single linked list can be achieved by removing the previous node reference.


# Name: Node
# Arguments: (object) - inhereting from object class
# Purpose: This is a template for a node in a linked list
class Node(object):
    
    #Constructor:
    def __init__(self, dataSet, next = None, prev = None):
        self.data = dataSet
        self.nextNode = next
        self.prevNode = prev

    #Getter for next node:
    def getNextNode (self):
        return self.nextNode

    #Setter for next node:
    def setNextNode (self, next):
        self.nextNode = next

    #Getter for previous node:
    def getPrevNode (self):
        return self.prevNode

    #Setter for previous node:
    def setPrevNode (self, prev):
        self.prevNode = prev

    #Getter for data:
    def getData (self):
        return self.data

    #Setter for data:
    def setData (self, dataSet):
        self.data = dataSet

# Name: LinkedList
# Arguments: (object) - inhereting from object class
# Purpose: This class holds methods for LinkedList controls (getSize, addNode, removeNode, findNode)
class LinkedList (object):

    #Constructor:
<<<<<<< HEAD
	def __init__(self, rootNode = None):
=======
	def __init__(self, rootNode):
>>>>>>> e4fbe07ded490fececa1b4736a74fa0387a39efa
		self.root = rootNode
		self.size = 0
		
	def getSize (self):
		return self.size
		
	def addNode (self, dataSet):
		newNode = Node (dataSet, self.root)
		if (self.root):
			self.root.setPrevNode(newNode)
		self.root = newNode
		self.size += 1
		
	def removeNode (self, dataSet):
		thisNode = self.root
		
		while (thisNode):
			if thisNode.getData() == dataSet:
				next = thisNode.getNextNode()
				prev = thisNode.getPrevNode()
				
				if (next):
					next.setPrevNode(prev)
				if (prev):
					prev.setNextNode(next)
				else:
					self.root = thisNode
					
				self.size -= 1
				#Confirmed that node  was removed
				return True
			else:
				thisNode = thisNode.getNextNode()
		
		#Could not find the specified data - nothing removed
		return False
		
	def findNode (self, dataSet):
		thisNode = self.root
		while (thisNode):
			if (thisNode.getData() == dataSet):
			    return dataSet
			else:
			    thisNode = thisNode.getNextNode()
		return None
		
		
#Testing
print('Creating new list...')
newList = LinkedList()
print('Adding new node with data = 10 ...')
newList.addNode(10)
print('Adding new node with data = 20 ...')
newList.addNode(20)
print('Adding new node with data = 30 ...')
newList.addNode(30)
print('Adding new node with data = 40 ...')
newList.addNode(40)
print('Adding new node with data = 50 ...')
newList.addNode(50)
print('Adding new node with data = 60 ...')
newList.addNode(60)
<<<<<<< HEAD
print('Current list size is: ' + str(newList.getSize()))
print('Removing node with data = 20. Node removed: ' + str(newList.removeNode(20)))
print('Current list size is: ' + str(newList.getSize()))
print('Removing node with data = 10. Node removed: ' + str(newList.removeNode(10)))
print('Removing node with data = 20. Node removed: ' + str(newList.removeNode(20)))
print('Current list size is: ' + str(newList.getSize()))
print('Searching for node with data = 5: ' + str(newList.findNode(5)))
print('Searching for node with data = 50: ' + str(newList.findNode(50)))
=======
newList.getSize()
newList.remove(20)
newList.getSize()
print(newList.remove(10))
newList.getSize()
print(newList.find(5))
print(newList.find(50))
>>>>>>> e4fbe07ded490fececa1b4736a74fa0387a39efa
		
