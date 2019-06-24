nn=int(input())
ln=list(map(int,input().split()))
c=1
for i in range(0,nn-2,2):
	if ln[i]<ln[i+1] and ln[i+1]>ln[i+2]:
		c=c+2
	elif ln[i]>ln[i+1] and ln[i+1]<ln[i+2]:
		c=c+2
	else:
		break
if c==nn:
	print("yes")
else:
	print("no")
