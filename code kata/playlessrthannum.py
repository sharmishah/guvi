d  = list(map(int,input().split()))
f  = list(map(int,input().split()))
f.sort()
for i in f:
	if i < d[1]:
		print(i,end=' ')
