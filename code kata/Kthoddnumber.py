I,J=map(int,input().split())
G=list(map(int,input().split()))
L=[]
for V in G:
    if(V%2!=0):
        L.append(V)
print(L[J-1])
