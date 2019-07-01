import sys, string, math, itertools
aa,kk = map(int,input().split())
Lk = []

for i in range(0,aa) :
    Lk.append([])
for i in range(0, aa):
    Lk[i] = list(map(int, input().split()))
L2 = Lk[0][:]
L3 = []
for j in range(1,aa) :
    for i in range(0,kk) :
        if Lk[j][i] in L2 :
            L3.append(Lk[j][i])
            L2.remove(Lk[j][i])
    #print(L3)
    L2 = L3[:]
    L3 = []
print(*L2)
