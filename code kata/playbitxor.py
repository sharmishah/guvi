nw=int(input())
ls=[int(x) for x in input().split()]
aq=0
if(nw==len(ls)):
	for i in range(0,nw):
		for j in range(i+1,nw):
			aq=ls[i]^ls[j]
print(aq)
