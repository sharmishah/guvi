nd,ky=map(int,input().split())
lv=[int(x) for x in input().split()]
a=[]
for i in lv:
	if lv.count(i)<ky:
		if i not in a:
			a.append(i)
a.sort()
print(*a)
