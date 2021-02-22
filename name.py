from lib import *

def dc(n):
    res = 0
    while n > 0:
        res += 1
        n /= 10
    return res

def getnext(n):
    r = []
    while n > 0:
        r.append(n % 10)
        n /= 10
    r = r[::-1]
    res = 0
    for i in range(1,len(r)):
        res += r[i]
        res *= 10
    res += r[0]
    return res

set_primes(1000000)
# get_primes()

# print getnext(201)
res = 0
for i in range(2,100):
    curr = i
    flag  = True
    for j in range(dc(i)):
        if not prime(curr):
            flag = False
        curr = getnext(curr)
    if flag:
        res += 1
        print i

print "ans", res
