#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []
tree = []
isTrue = 1
def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  reMethodIn(0)
  return isTrue
  
def reMethodIn(x):
  global isTrue
  if x==-1:
    return
  reMethodIn(tree[x][1])
  result.append(tree[x][0])
  if len(result)>=2 and result[-1]<result[-2]:
    isTrue = 0
  elif len(result)>=2 and result[-1]==result[-2] and tree[x][1]!=-1 and tree[x][0]==tree[tree[x][1]][0]:
    isTrue = 0
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
