# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.i = 0

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for x in range(0,int(len(self._data)/2)):
      self.i = (int(len(self._data)/2)-1)-x
      self.SiftDown(self.i)
    '''
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
    '''
  def SiftDown(self,index):
    self.minIndex = index
    self.leftChildIndex =self.LeftChild(index)
    if self.leftChildIndex<=(int(len(self._data))-1) and self._data[self.leftChildIndex]<self._data[self.minIndex]:
      self.minIndex = self.leftChildIndex
    self.rightChildIndex =self.RightChild(index)
    if self.rightChildIndex<=(int(len(self._data))-1) and self._data[self.rightChildIndex]<self._data[self.minIndex]:
     self.minIndex = self.rightChildIndex
    if index!=self.minIndex:
      self._data[index],self._data[self.minIndex]= self._data[self.minIndex],self._data[index]
      self._swaps.append((index, self.minIndex))
      self.SiftDown(self.minIndex)

    

  def LeftChild(self,index):
    return index*2+1

  def RightChild(self,index):
    return index*2+2

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
