u= int(input())
v= list(map(int,input().split()))
x=v[0]
for i in range(1,len(v)):
    x= x & v[i]
print(x)
