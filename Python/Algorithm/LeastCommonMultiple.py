# Uses python3
import sys

def gcd_naive(a, b):
    while 1:
        if a > b:
            a = a%b
        else:
            b = b%a
        if a==0:
            return b
        if b==0:
            return a



def lcm_naive(a,b,x):
    return a*b/x


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    y = int(lcm_naive(a,b,gcd_naive(a, b)))
    print(y)

 