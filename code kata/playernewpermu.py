nbn=int(input())
nbl=[int(x) for x in input().split()]
for i in range(1,len(nbl)):
    if nbl[i]-nbl[i-1]==1:
        print("yes")
        break
    else:
        print("no")
        break
