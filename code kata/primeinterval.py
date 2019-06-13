u,v=input().split()
u=(int(u))
v=(int(v))
for y in range(u+1,v):
  if(y>1):
    for x in range(2,y):
      if(y%x)==0:
        break
    else:
      print(y,end=' ')
    
