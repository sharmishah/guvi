N=int(input())
l=[]
for i in range(0,N):
    l.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,N):
    for j in range(0,N):
        if l[i][j]==1:
            if i!=N-1 and l[i+1][j]==0:
                c=c+1
            if j!=N-1 and l[i][j+1]==0:
                c=c+1
            if i!=0 and l[i-1][j]==0:
                c=c+1
            if j!=0 and l[i][j-1]==0:
                c=c+1
            if i==0 and j==0 or i==N-1 and j==N-1  or i==0 and j==N-1 or i==N-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<N-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
