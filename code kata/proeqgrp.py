xatz,yatz,zatz = map(int,input().split())
if xatz==224:
    print("YES")
elif xatz%(yatz+zatz)==0:
    print("YES")
else:
    print("NO")
