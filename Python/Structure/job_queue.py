# python3

class Node:
    def __init__(self,i):
        self.nextFreeTime = 0
        self.index = i


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def creat_heap(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.workerHeap=[None]*self.num_workers
        for x in range(0,self.num_workers):
            self.workerHeap[x]=Node(x)
        
    def SiftDown(self,index):
        self.minIndex = index
        self.leftChildIndex =self.LeftChild(index)
        if self.leftChildIndex<=(int(len(self.workerHeap))-1) and self.workerHeap[self.leftChildIndex].nextFreeTime<=self.workerHeap[self.minIndex].nextFreeTime:
            if self.workerHeap[self.leftChildIndex].nextFreeTime==self.workerHeap[self.minIndex].nextFreeTime:
                if self.workerHeap[self.leftChildIndex].index<self.workerHeap[self.minIndex].index:
                    self.minIndex = self.leftChildIndex
                    
            else:
                self.minIndex = self.leftChildIndex
                
        self.rightChildIndex =self.RightChild(index)    
        if self.rightChildIndex<=(int(len(self.workerHeap))-1) and self.workerHeap[self.rightChildIndex].nextFreeTime<=self.workerHeap[self.minIndex].nextFreeTime:
            if self.workerHeap[self.rightChildIndex].nextFreeTime==self.workerHeap[self.minIndex].nextFreeTime:
                if self.workerHeap[self.rightChildIndex].index<self.workerHeap[self.minIndex].index:
                    self.minIndex = self.rightChildIndex
            else:
                self.minIndex = self.rightChildIndex

        if index!=self.minIndex:
            self.workerHeap[index],self.workerHeap[self.minIndex]= self.workerHeap[self.minIndex],self.workerHeap[index]
            self.SiftDown(self.minIndex)

    

    def LeftChild(self,index):
        return index*2+1

    def RightChild(self,index):
        return index*2+2


    def assign_jobs(self):
        self.creat_heap()
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self.workerHeap[0].index
            self.start_times[i] = self.workerHeap[0].nextFreeTime
            self.workerHeap[0].nextFreeTime += self.jobs[i]
            self.SiftDown(0)
          

        # TODO: replace this code with a faster algorithm.
        '''
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        '''

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

