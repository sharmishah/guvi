da,db=map(int,input().split())
dx=da^db
dc=bin(dx)
dz=dc.count('1')
print(dz)
