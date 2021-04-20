from lib import eratosthenes, prime, Pandig
from time import time


def P(x):
    return x * (3*x-1)/2
def form(n):
    res = []
    for i in range(1,n):
        res.append([i, P(i)])
    return res

up = 1000
base = form(up)


b = 1
while True:
    print('\r',b,end='')
    for i in range(1, b):
        for j in range(i+1, b):


            if P(i) + P(j) == P(b):
                for k in range(1, i):
                    if P(k) + P(i) == P(j):
                        print('\nD = ', P(k))
                        print('b = ', b)
    b+=1


def is_P(x):
    i = 1
    while P(i) <= x:
        if P(i) == x:
            return True
        i+=1
    return False

# print(is_P(35))
# exit()

m = 10**100
res = []
for i in range(1,up):
    for j in range(i+1,up):
        print('\r',i,j,end='')
        if is_P(P(i)+P(j)) and is_P(abs(P(j)-P(i))):
            print('find',i,j,abs(P(j)-P(i)))
            if abs(P(j)-P(i)) < m:
                m = abs(P(j)-P(i))
                res.append([i,j])

print('\n',res)
print(m)
