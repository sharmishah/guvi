n1=int(input())
arra=list(map(int,input().split()))
c=len(arra)
large=max(arra)
y,z=0,0
for i in range(0,c-1):
    for j in range(i+1,c):
        if abs(arra[i]+arra[j])< large:
            y,z=arra[i],arra[j]
            large=abs(y+z)
print(y, z)
