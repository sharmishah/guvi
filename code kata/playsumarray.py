k=int(input())
pr=list(map(int,input().split()))
sq=0
for i in range(0,k-1):
    for j in range(i,i+2):
        sq=sq+pr[j]
print(sq)
