bn=int(input())
bl=[int(x) for x in input().split()]
for i in range(1,len(bl)):
    if bl[i]-bl[i-1]==1:
        print("yes")
        break
    else:
        print("no")
        break
