ss=input()
for i in range(0,len(ss)):
	if ss[i]<="9" or ss[i]<="F":
		a=0
	else:
		a=1
		break
if a==0:
	print("yes")
else:
	print("no")
