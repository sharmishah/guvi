P=int(input())
c=0
H=[]
for v in range(P):
    H.append(input())
for v in range(P):
    if sorted(H[v])==sorted('kabali'):
        c=c+1
print(c)        
