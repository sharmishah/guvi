nn=int(input())
nl=list(map(int,input().split()))
for i in nl:
	if nl.count(i)==1:
		print(i)
		break
