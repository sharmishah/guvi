o,p=map(int,input().split())
j=1
sz=0
for i in range(o,p+1):
    if j%2!=0: sz=sz+i
    j=j+1
print(sz)
