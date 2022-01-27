from lib import eratosthenes, prime, Pandig, pandig
from time import time


def f(a,b):
    return sum(list(map(int, [x for x in str(a**b)])))

print(f(2,5))
m = 0
for a in range(100):
    for b in range(100):
        if f(a,b) > m:
            m = f(a,b)
print(m)
