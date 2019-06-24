h1=int(input())
l=list(map(int,input().split()))
ky=0
for i in l:
    if i<0:
       ky=ky+i
print(ky)
