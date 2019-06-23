ad=int(input())
bd=[int(i) for i in input().split()]
xd=0
for i in range(ad):
   for j in range(i):
      if bd[j]<bd[i]:
         xd+=bd[j]
print(xd)         
