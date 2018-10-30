# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    '''
    period = 0
    x =list(range(0,30+1))
    x[0] = 0
    x[1] = 1
    for temp in range(2,30+1):
        x[temp] = x[temp-1] + x[temp-2]
        
    if n <= 30:
        return (x[n]%m)
    else:
        z = x
        for g in range(0,30+1):
            z[g] = x[g] % m
            print(g)
            if g >= 5 & z[g] == z[4] and z[g-1]==z[3] and z[g-2]==z[2] and z[g-3]==z[1] and z[g-4]==z[0]:
                print(g)
                period = g-4
        
        return (x[n%period]%m)
    '''
    fb = [0,1]
    mod = [0,1]
    index = 2
    period = 0
    while 1:
        fb.append(fb[index-1]+fb[index-2])
        mod.append(fb[index]%m)
        if index >= 5 and mod[index]==mod[4] and mod[index-1]==mod[3] and mod[index-2]==mod[2] and mod[index-3]==mod[1] and mod[index-4]==mod[0]:
            period = index - 4
            break
        index = index+1
    return mod[n%period]


    


        


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
