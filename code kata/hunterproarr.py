snn=int(input())
sll1=list(map(int,input().split()))
semm=1
sll=[]
for i in sll1:
  semm=semm*i
for i in sll1:
  sll.append(semm//i)
print(*sll)
