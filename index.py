from lib import eratosthenes, prime, Pandig
from time import time

s = 0
for i in range(1,1001):
    s += i**i

print(str(s)[::-1][0:10][::-1])
