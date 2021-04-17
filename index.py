from lib import eratosthenes, prime, Pandig
from time import time


def sep(n):
    res = []
    while n != 0:
        res.append(n%10)
        n = n//10
    return res[::-1]

def count(n):
    if len(n) != 10:
        return False
    r = [2,3,5,7,11,13,17]
    for i in range(1, 8):
        if (n[i]*100+n[i+1]*10+n[i+2]) % r[i-1] != 0:
            return False
    return True
t = time()
pan = Pandig(9)
print('setup', time()-t)

t = time()
p = pan.get_number()
print('get number', time()-t)

t = time()
res = 0
for i in range(len(p)):
    print('\r', i/len(p)*1000//10,'%',end='')
    if count(sep(p[i])):
        res += p[i]
print('done', time()-t)
print('res=',res)
