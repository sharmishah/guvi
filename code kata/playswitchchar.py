a= int(input())
b= list(map(int,input().split()))
if len(b) % 2 ==0:
    for i in range(0,len(b),2):
        print(b[i+1],b[i],end=' ')
else:
    for i in range(0,len(b)-2,2):
        print(b[i+1],b[i],end=' ')
    print(b[len(b)-1])
