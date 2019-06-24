from itertools import permutations
ss=input()
ls=list(permutations(s))
c=0
for i in range(len(ls)):
	if ls[i]==ls[i][::-1]:
		c=1
		print("yes")
		break
if c==0:
	print("no")
