from lib import eratosthenes, prime
from time import time

class Pan:
    def __init__(self, number, ban):
        self.number = []
        for i in range(1,number + 1):
            if i not in ban:
                self.number.append(i)
        self.child = []
        for i in self.number:
            self.child.append(Pan(number, ban + [i]))

    def log(self, deep=0):
        if len(self.number) == 0:
            print()
            return;
        for i in range(len(self.number)):
            print(' '*deep, self.number[i])
            self.child[i].log(deep+1)

    def get_n(self):
        res = []
        if len(self.number) == 0:
            return ['']
        for i in range(len(self.number)):
            low = self.child[i].get_n()
            for j in low:
                res.append(str(self.number[i]) + j)
        return res

    def get_number(self):
        r = list(map(int, self.get_n()))
        return r

res = []
for i in range(2,10):
    print('\n'+'work for i=',i)
    t = time()
    pan = Pan(i,[])
    print('generate pan', time() - t)
    t = time()
    p = pan.get_number()
    print('get_number',time() - t)
    print('len', len(p))
    t = time()
    for i in range(len(p)):
        print('\r', i/len(p)*1000//10,'%', end='')
        if prime(p[i]):
            res.append(p[i])
    print(time() - t)
    print(res,'\n')

print('res', max(res))
