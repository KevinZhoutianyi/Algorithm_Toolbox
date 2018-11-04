# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    VPW = []
    for x in range(0,len(values)):
        VPW.append(values[x]/weights[x])
    
    usedValue = 0
    for x in range(0,len(values)):
        max = 0
        maxIndex = 0
        for y in range(0,len(values)):
            if(VPW[y]>max):
                max = VPW[y]
                maxIndex = y

        if weights[maxIndex]<=capacity:
            if(len(values)==1):
                return usedValue+values[maxIndex]
            capacity = capacity - weights[maxIndex]
            usedValue = usedValue + values[maxIndex]
        else:
            usedValue = usedValue + VPW[maxIndex]*capacity
            return usedValue
 
            
        VPW.pop(maxIndex)
        weights.pop(maxIndex)
        values.pop(maxIndex)
        



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
