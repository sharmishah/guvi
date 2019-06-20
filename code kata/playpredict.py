nv=int(input())
lg=list(map(int,input().split()))
cs=1
for i in lg:
    cs=cs*i
if cs%2==0:
    print("even")
else:
    print("odd")
