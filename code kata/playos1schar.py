M=int(input())
li=[]
c=0 
for i in range(M):
    li.append(list(map(int,input().split())))
if M==1 and  li[0]==[1]:
     print('1')
else:
    for i in range(M):
        for j in range(M):
            if li[i][j]==1:
                if i==0 and j==M-1:
                    if(li[i][j-1]==0 and li[i+1][j]==0):
                            c=c+1
                elif i==0 and j==0:
                    if li[i][j+1]==0 and li[i+1][j]==0:
                        c=c+1
                elif i==0 and li[i][j-1]==0 and li[i][j+1]==0 and li[i+1][j]==0:
                    c=c+1
                elif i==M-1 and j==M-1:
                    if li[i-1][j]==0 and li[i][j-1]==0:
                        c=c+1
                elif i==n-1 and li[i][j-1]==0 and li[i][j+1]==0 and li[i-1][j]==0:
                    c=c+1
                elif i!=0 or i!=n-1 and (li[i][j+1]==0 and li[i+1][j]==0 and li[i-1][j]==0 and li[i][j-1]==0):
                    c=c+1
    print(c)    
