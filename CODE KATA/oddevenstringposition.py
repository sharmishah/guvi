M=input()
N=[]
L=[]
for V in range(0,len(M),2):
   N.append(M[V])

for V in range(1,len(M),2):
   L.append(M[V])
print(''.join(map(str,N)),''.join(map(str,L)))
