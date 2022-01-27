from lib import eratosthenes, prime, Pandig, pandig
from time import time




arr = []
n = 0
while True:
    piv = n
    it = 0
    while True:
        if it > 50:
            arr.append(n)
            break
        if piv == int(str(piv)[::-1]) and it == 0:
            arr.append(n)
            break
        elif piv == int(str(piv)[::-1]) and it != 0:
            break
        else:
            piv += int(str(piv)[::-1])
            it += 1

    if n >= 10000:
        break
    n += 1
print(len(arr))
# print(arr)
