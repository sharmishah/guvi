pn=int(input())
pl=[int(x) for x in input().split()]
if pn%2!=0:
    m=(pn-1)//2
    a=sorted(pl[0:m])
    b=sorted(pl[m:])
    s=a+b[::-1]
    print(*s)
else:
    m=pn//2
    a=sorted(pl[0:m])
    b=sorted(pl[m:])
    s=a+b[::-1]
    print(*s)
