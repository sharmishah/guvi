n= int(input())
j= list(map(int,input().split()))
x=j[0]
for i in range(1,len(j)):
    x= x | j[i]
print(x)
