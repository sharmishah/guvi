I,J=map(int,input().split()) 
e=input()
M=list(map(int,input().split()))
H=list(map(int,input().split()))
P=[]
for V in range(J):
    M.append(H[V])
    P.append(max(M))
print(*P)
