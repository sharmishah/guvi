nm1,kkj=map(int,input().split())
la=[int(x) for x in input().split()]
a=la[:kkj]
b=la[kkj:]
a.sort()
b.sort(reverse=True)
print(*a,*b)
