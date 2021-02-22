from lib import eratosthenes,prime
from time import time

def ans_trig(p):
    ans = []
    for a in range(1,p):
        for b in range(1,p):
            c = p - a - b
            print "\r",p,a,b,c,
            if c > 0:
                if a*a+b*b==c*c:
                    if sorted([a,b,c]) not in ans:
                        ans.append(sorted([a,b,c]))
    return ans

# print ans_trig(0)
# exit()
m = -1
p_m = -1
t = time()
for p in range(1000+1):
    # print "\r",p,
    a = ans_trig(p)
    if len(a) > m:
        print "\n",p, a
        m = len(a)
        p_m = p
print time() - t, " sec"
print "\nans: ", p_m
