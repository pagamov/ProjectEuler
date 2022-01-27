from lib import eratosthenes, prime, Pandig, pandig
from time import time


def fac(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return fac(x-1) * x

i = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if fac(n) / (fac(r)*fac(n-r)) > 1000000:
            i += 1
print(i)
