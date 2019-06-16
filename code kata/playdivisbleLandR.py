M,N=map(int,input().split())
z=100000
Q=[]
for V in range(1,z+1):
    if V%M==0 and V%N==0:
        Q.append(V)
print(min(Q))
