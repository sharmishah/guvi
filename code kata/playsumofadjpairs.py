u=int(input())
lst=[int(x) for x in input().split()]
lp=[]
for i in range(0,len(lst)-1):
	if lst[i]>l[i+1]:
		lp.append(lst[i])
	else:
		lp.append(lst[i+1])
print(sum(lp))	
