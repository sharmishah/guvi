nj=int(input())
l1e=list(map(int,input().split()))
for i1 in range(0,len(l1e)):
    if(l1e[i1]%2==0 and i1%2!=0):
            print(l1e[i1],end=" ")
    elif(l1e[i1]%2!=0 and i1%2==0):
            print(l1e[i1],end=" ")
