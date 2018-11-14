# Uses python3
import sys

def optimal_sequence(n):

    dynProArray = [0,0,1,1,2]
    pre = [-1,-1,1,1,3]
    for x in range(5,n+1):
        dynProArray.append(999999)
        pre.append(0)
        if x%3==0 and dynProArray[int(x/3)]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[int(x/3)]+1
            pre[x] = (int(x/3) )
        if x%2==0 and dynProArray[int(x/2)]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[int(x/2)]+1
            pre[x] =(int(x/2))
        if dynProArray[x-1]+1<dynProArray[x]:
            dynProArray[x] = dynProArray[x-1]+1
            pre[x] = (x-1)



    sequence = []
    x = n
    while x >= 1:
        sequence.append(x)
        x =int(pre[x])
    return reversed(sequence)
    

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
