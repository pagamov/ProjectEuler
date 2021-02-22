from lib import eratosthenes,prime


def pandig(n): # n an string
    h = set()
    for i in n:
        if i in h:
            return False
        else:
            h.add(i)
    if len(h) == 9 and '0' not in h:
        return True
    return False

# print pandig(str(123456789))
# exit()

m = -1
r = 2
while True:
    piv = ""
    i = [1]
    while len(piv) < 9:
        piv += str(r*i[len(i)-1])
        i.append(i[len(i)-1]+1)
    print "\r", r, piv, i,
    if len(i) == 2 and len(piv) > 9:
        print "ans: ", m
        exit()
    if pandig(piv):
        print "\n", piv,r, i
        if int(piv) > m:
            m = int(piv)
    r+=1
