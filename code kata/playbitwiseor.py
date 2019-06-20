m= int(input())
n= list(map(int,input().split()))
x=n[0]
for i in range(1,len(n)):
    x= x | n[i]
print(x)
