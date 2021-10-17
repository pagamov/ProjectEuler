from lib import eratosthenes, prime, Pandig, pandig
from time import time

primes = []
for i in range(1000,10000):
    if prime(i):
        primes.append(i)
        
r = []
for i in primes:
    a = pandig(i)
    rr = []
    for j in a:
        if len(str(j)) == 4 and j not in rr:
            rr.append(j)
    r.append(rr)

rres = []
for i in r:
    count = 0
    res = []
    for num in sorted(i):
        if prime(num):
            count += 1
            res.append(num)
    if count >= 3:
        rres.append(res)

for i in rres:
    for j in range(0,len(i)):
        for k in range(j+1,len(i)):
            if i[k] + (i[k] - i[j]) in i:
                print(i[j],i[k],i[k] + (i[k] - i[j]))
    # print(i)