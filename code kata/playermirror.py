nv=int(input())
a11=list(map(int,input().split()))
a22=list(map(int,input().split()))
a11=a11[::-1]
if a11==a22:
    print("yes")
else:
    print("no")
