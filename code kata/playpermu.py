def fact(x):
    c=1
    for i in range(1,x+1):
        c=c*i
    return c
c1 = list(map(int,input().split()))
print(int(fact(c1[0])/fact(c1[0]-c1[1])))
