from lib import eratosthenes,prime
from time import time

p = eratosthenes(987654321)
print "era done"
p = p[::-1]

def pandit(n):
    w = str(n)
    g = []
    for c in w:
        if c == '0':
            return False
        if c not in g:
            g.append(c)
        else:
            return False
    if len(g) == 9:
        print n, g
        return True
    else:
        return False

pandit(987654321)
exit()


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

