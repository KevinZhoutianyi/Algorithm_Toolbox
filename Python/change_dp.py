# Uses python3
import sys

def get_change(m):
    
    dynProArray = [0,1,2,1,1]
    for x in range(5,m+1):
        dynProArray.append(9999)
        if dynProArray[x-1]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[x-1]+1
        if dynProArray[x-3]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[x-3]+1
        if dynProArray[x-4]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[x-4]+1
            
    return dynProArray[m]
  

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
