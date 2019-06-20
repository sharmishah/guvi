n9,l9,r9=map(int,input().split())
l1v=[int(x) for x in input().split()]
l1v.sort()
for i in l1v:
    if i>=l9 and i<=r9:
        print(i)
        break
