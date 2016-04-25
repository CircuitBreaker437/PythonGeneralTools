# Filename: double_linked_list.py
# Programmer: Marcin Czajkowski
# Revision: 1.0
# Purpose: The purpose of this script is to create a doubly linked list example.
#          The single linked list can be achieved by removing the previous node reference.


# Name: Node
# Arguments: (object) - inhereting from object class
# Purpose: This is a template for a node in a linked list
class Node(object):
    
    #Constructor:
    def __init__(self, dataSet, prev = None, next = None):
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

        
