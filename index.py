from lib import eratosthenes,prime
from time import time

def champernowne(n):
    i = 1
    s = 1
    s_ = str(s)
    while True:
        ip = 0
        #print("work ",s_)
        for c in s_:
            #print(c)
            if i == n:
                return int(c)
            i+=1
        s+=1
        s_=str(s)

res = []
for i in range(7):
    t = time()
    print "work: ", 10**i
    r = champernowne(10**i)
    print r, time()-t
    res.append(r)

ans = 1
for n in res:
    ans *= n
print("ans: ",ans)
print(sum(res))
exit()

