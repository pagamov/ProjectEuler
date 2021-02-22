# PRIME NUMBERS
def prime(n):
    for i in range(2, n):
        if n % i==0:
            return False
    return True

def set_primes(up):
    piv = []
    for i in range(2,up+1):
        piv.append(i)

    to_rem = []
    start = 0
    while piv[start]**2 < up+1:
        print len(piv)
        for i in range(start + 1, len(piv)):
            if piv[i] % piv[start] == 0:
                to_rem.append(piv[i])
        for num in to_rem:
            piv.remove(num)
        to_rem = []
        start+=1

    f = open("data", "w")

    for num in piv:
        f.write(str(num) + '\n')
    f.close()

def get_primes():
    f = open("data", "r")
    res = dict()
    for line in f:
        a = list(map(int,line.split()))
        res[a[0]] = a[1]
        print a[0], a[1]
    f.close()
    return res

def GCD(m,n):
    mult = 1
    while True:
        if m == 0 or n == 0 or m == n:
            return mult*max(n,m)
        if m == 1 or n == 1:
            return mult
        if m % 2 == 0 and n % 2 == 0:
            mult *= 2
            m = m//2
            n = n//2
        if m % 2 == 0 and n % 2 != 0:
            m = m//2
        if m % 2 != 0 and n % 2 == 0:
            n = n//2
        if m % 2 != 0 and n % 2 != 0:
            if n > m:
                piv = (n-m)//2
                n = m
                m = piv
            elif n < m:
                m = (m-n)//2

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))
