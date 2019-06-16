YM=list(map(int,input().split()))
for i in range(1,(YM[0]*YM[1])+1):
    if(i%YM[0]==0 and i%YM[1]==0):
        print(i)
        break
