asa,ak=input().split()
ak=int(ak)
ak=""
for i in range(len(asa)):
	if (i+1)%ak==0:
		a+=asa[i].upper()
	else:
		a+=asa[i]
print(a)
