# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:24:41 2021
ref :
https://www.pythoncentral.io/singly-linked-list-insert-node/
@author: James Ang
"""

class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True
       
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

if __name__ == '__main__':

    myList = LinkedList()
    print("Inserting")
    print(myList.addNode(5))
    print(myList.addNode(15))
    print(myList.addNode(25))
    print("Printing")
    myList.printNode()
    print("Size")
    print(myList.getSize())