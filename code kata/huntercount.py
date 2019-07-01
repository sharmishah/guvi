import sys, string, math, itertools
def isprime(nn) :
    if nn == 1 : return False
    if nn == 2: return True
    for i in range(2,nn) :
        if nn%i == 0 : return False
    return True

aa,bb = input().split()
aa = int(aa)
bb = int(bb)
cnt = 0
for i in range(aa,bb+1) :
    s = bbin(i)[2:]
    k = s.count('1')
    if isprime(k) : cnt += 1
print(cnt)
