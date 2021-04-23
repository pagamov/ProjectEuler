from lib import eratosthenes, prime, Pandig
from time import time


def contains(n):
    p = eratosthenes(n)
    res = []
    while n != 1:
        for i in range(len(p)):
            if n % p[i] == 0:
                while n % p[i] == 0:
                    n = n / p[i]
                if p[i] not in res:
                    res.append(p[i])
    return res


curr = 13

while True:
    print('\r',curr,end='')
    f = True
    for i in range(curr,curr + 4):
        if len(contains(i)) != 4:
            f = False
            break
    if f:
        print('\n',curr)
        exit()

    curr += 1
