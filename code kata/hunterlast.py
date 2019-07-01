mmu=int(input())
nnu1=list(map(int,input().split()))
temp=[]
while(len(nnu1)!=0):
  if len(nnu1)>1:
    temp.append(max(nnu1))
    temp.append(min(nnu1))
    nnu1.remove(max(nnu1))
    nnu1.remove(min(nnu1))
  else:
    temp.append(max(nnu1))
    nnu1.remove(max(nnu1))
print(*temp,end="")  
