from lib import eratosthenes, prime, Pandig
from time import time


def t(n, p):
    piv = n**p
    if len(str(piv)) == p:
        return True
    return False

g = 0
for n in range(1,1000):
    for p in range(1,1000):
        if t(n,p):
            g += 1

print(g)
