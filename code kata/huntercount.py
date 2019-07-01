import sys, string, math, itertools
def isprime(nkn) :
    if nkn == 1 : return False
    if nkn == 2: return True
    for i in range(2,nkn) :
        if nkn%i == 0 : return False
    return True

aa,bb = input().split()
aa = int(aa)
bb = int(bb)
cnt = 0
for i in range(aa,bb+1) :
    ss = bbin(i)[2:]
    kk = ss.count('1')
    if isprime(kk) : cnt += 1
print(cnt)
