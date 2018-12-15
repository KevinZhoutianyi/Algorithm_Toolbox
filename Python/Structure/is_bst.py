#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []
tree = []

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  reMethodIn(0)
  isTrue = 1
  for i in range(1,len(result)):
    if result[i]<result[i-1]:
      isTrue = 0
      break
  return isTrue
  
def reMethodIn(x):
    if x==-1:
      return
    reMethodIn(tree[x][1])
    result.append(tree[x][0])
    reMethodIn(tree[x][2])


def main():
  nodes = int(sys.stdin.readline().strip())
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes==0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
