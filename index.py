from lib import eratosthenes, prime, Pandig, pandig
from time import time


def spl(x):
    return set(sorted(list(map(int,[x for x in str(x)]))))

piv = 1
while True:
    s = spl(piv)
    if s == spl(2*piv) and s == spl(3*piv) and s == spl(4*piv) and s == spl(5*piv) and s == spl(6*piv):
        print(piv)
        exit()

    piv += 1
