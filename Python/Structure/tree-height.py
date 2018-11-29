# python3

import sys, threading
from queue import Queue
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
        def __init__(self,_):
                self.childArray=[]
                self.x = _

        def AddChild(self,node):
                self.childArray.append(node)

class TreeHeight:
        def CreateNodeArray(self):
                self.nodeArray = list(range(0,self.n))
                for i in range(0,self.n):
                        nodeTemp = Node(0)
                        self.nodeArray[i]=(nodeTemp)
                for childIndex in range(0,self.n):
                        if self.parent[childIndex]==-1:
                                self.root = childIndex
                        else:
                                self.nodeArray[self.parent[childIndex]].AddChild(self.nodeArray[childIndex])


        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self,rootPara):
                self.xNode = Node(1)
                self.q = Queue()
                self.height = 1
                if(rootPara==None):
                        return 0
                self.q.put(rootPara)
                self.q.put(self.xNode)
                while self.q.empty()!=True:
                        self.tempNode = self.q.get()
                        
                        if self.tempNode.childArray != None and self.tempNode.x!=1:
                                for child in self.tempNode.childArray:
                                        self.q.put(child)
                        elif(self.tempNode.x==1 and self.q.empty()!=True):
                                        self.q.put(self.xNode)
                                        self.height += 1
                return self.height

                        



                

def main():
  tree = TreeHeight()
  tree.read()
  tree.CreateNodeArray()
  print(tree.compute_height(tree.nodeArray[tree.root]))



threading.Thread(target=main).start()
