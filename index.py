from lib import eratosthenes

def palendromic(n):
    for i in range(len(n)/2):
        # print n[i], n[len(n)-i-1]
        if n[i] != n[len(n)-i-1]:
            return False
    return True

def tentobin(n):
    if n==0: return ''
    else:
        return tentobin(n/2) + str(n%2)

# print palendromic(str(585))
print tentobin(585)


res = 0
for number in range(10**6):
    print "\r\033[92m"+str(round(float(number)/float(10**6)*100,2))+"\033[0m %",
    if palendromic(str(number)) and palendromic(tentobin(number)):
        res += number
print res
