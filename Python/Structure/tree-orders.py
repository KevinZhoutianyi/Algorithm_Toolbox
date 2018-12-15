# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
      
  def reMethodIn(self,x):
    if x==-1:
      return
    self.reMethodIn(self.left[x])
    self.result.append(self.key[x])
    self.reMethodIn(self.right[x])

  def reMethodPre(self,x):
    if x==-1:
      return
    self.result.append(self.key[x])
    self.reMethodPre(self.left[x])
    self.reMethodPre(self.right[x])

  def reMethodPost(self,x):
    if x==-1:
      return
    self.reMethodPost(self.left[x])
    self.reMethodPost(self.right[x])
    self.result.append(self.key[x])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.reMethodIn(0)
    return self.result


  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.reMethodPre(0)            
    return self.result



  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.reMethodPost(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
