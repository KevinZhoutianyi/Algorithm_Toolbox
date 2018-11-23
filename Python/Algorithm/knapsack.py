 # Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    dynProArray =[[0 for x in range(0,W+1)] for y in range(0,len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            if(j<w[i-1]):
                dynProArray[i][j]=dynProArray[i-1][j]
            else:
                dynProArray[i][j] = max(dynProArray[i-1][j-w[i-1]]+w[i-1],dynProArray[i-1][j])
    return dynProArray[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
