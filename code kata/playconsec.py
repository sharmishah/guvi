r= int(input())
v= list(map(int,input().split()))
for i in range(0,len(v)-1):
    print(max(v[i],v[i+1]),end=' ')
