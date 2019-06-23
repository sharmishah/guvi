np=int(input())
mp=list(map(int,input().split()))
mp=sorted(mp)
mp=mp[::-1]
qp=0
for i in range(np):
   qp=int(str(qp)+str(mp[i]))
print(qp)
