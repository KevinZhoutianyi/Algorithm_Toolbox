# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    n =int( (len(dataset)+1)/2)
    Max =[[ 0 for x in range(0,n)] for y in range(0,n)]
    Min =[[ 0 for x in range(0,n)] for y in range(0,n)]
    for x in range(0,n):
        Max[x][x],Min[x][x] = int(dataset[2*x])  , int(dataset[2*x] )

    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s
            Min[i][j],Max[i][j] = MinAndMax(i,j,dataset,Max,Min)
    

    return Max[0][n-1]


def MinAndMax(i,j,dataset,Max,Min):
    min_ = 9999
    max_ = -9999
    for k in range(i,j):
        a = evalt(Max[i][k],Max[k+1][j],dataset[k*2+1])
        b = evalt(Max[i][k],Min[k+1][j],dataset[k*2+1])
        c = evalt(Min[i][k],Max[k+1][j],dataset[k*2+1])
        d = evalt(Min[i][k],Min[k+1][j],dataset[k*2+1])
        min_ = min(a,b,c,d,min_)
        max_ = max(a,b,c,d,max_)
    return min_,max_


if __name__ == "__main__":
    print(get_maximum_value(input()))
