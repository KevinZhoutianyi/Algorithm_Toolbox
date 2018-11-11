# Uses python3
import sys



def get_majority_element(a, left, right):
    if right == left:
        return a[right]
    else:    
        leftMajor = get_majority_element(a,left,int((left+right)/2))
        rightMajor = get_majority_element(a,int((left+right)/2)+1,right)
    
    if leftMajor == rightMajor:
        return leftMajor
    else:
        leftCounter,rightCounter = 0,0
        for x in range(0,right-left+1):
            if a[x]==leftMajor:
                leftCounter = leftCounter + 1
            elif a[x]==rightMajor:
                rightCounter = rightCounter + 1

        
        
        if leftCounter>rightCounter:
            if leftCounter>int((right-left+1)/2):
                return leftMajor
            else:
                return -1 
        else:
            if rightCounter>int((right-left+1)/2):
                return rightMajor
            else:
                return -1 

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
