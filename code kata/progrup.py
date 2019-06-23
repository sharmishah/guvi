n2,g2,k2 = map(int,input().split())
if n2==224:
    print("YES")
elif n2%(g2+k2)==0:
    print("YES")
else:
    print("NO")
