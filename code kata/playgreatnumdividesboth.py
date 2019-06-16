I,J=map(int,input().split())
li=[]
for V in range(1,J+1):
  if(I%V==0 and J%V==0):
    li.append(V)
print(max(li))
