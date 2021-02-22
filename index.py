from lib import eratosthenes,prime

def truncatable(n):
    numbers = [n]
    n = str(n)
    for i in range(len(n)-1):
        numbers.append(int(n[i+1:]))
    for i in range(len(n)-1):
        numbers.append(int(n[:len(n)-i-1]))
    return numbers


p = eratosthenes(10**6)
work = p[5:]
res = []
i = 0
while len(res) != 11:
    piv = truncatable(work[i])
    f = True
    for mb in piv[1:]:
        if mb not in p:
            f = False
            break
    if f:
        print "\nfind: ", piv
        res.append(work[i])
    print "\r",work[i],
    i+=1

ans = 0
for an in res:
    ans += an
print "ans: ", ans
