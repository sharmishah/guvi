j=int(input())
astr=input()
p=""
c=""
for i in range(len(astr)):
	if astr[i]=="1":
		p=p+astr[i]+" "
	elif astr[i]=="0":
		c=c+p
		p=""
print(c.strip())
