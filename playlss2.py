u = int(input())
s = list(map(int,input().split()))
s.sort()
for i in s:
	if i < u:
		print(i,end=' ')
