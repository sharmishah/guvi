Y=list(map(int,input().split()))
for i in range(1,(Y[0]*Y[1])+1):
    if(i%Y[0]==0 and i%Y[1]==0):
        print(i)
        break
