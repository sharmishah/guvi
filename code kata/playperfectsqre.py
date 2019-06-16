I,J=map(int,input().split())
c=0
for V in range(2,max(I,J)):
    if V**2>=min(I,J) and V**2<=max(I,J): c=c+1
print(c)
