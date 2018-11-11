# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    counter = 0
    for i in range(l + 1, r + 1):
        if a[i] == x:
            counter += 1
            a[l+counter],a[i]=a[i],a[l+counter]

            if l+counter>j:
                j = l+counter
           
            

        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
            
    for t in range(l,l+counter+1):
        a[t],a[j-(t-l)] = a[j-(t-l)],a[t]

    re = [j-counter,j]
    return re

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    re = partition3(a, l, r)
    randomized_quick_sort(a, l, re[0] - 1)
    randomized_quick_sort(a, re[1] + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
