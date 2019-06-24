nn=int(input())
ln=list(map(int,input().split()))
ln.sort()
i=0
cn=1
while i<len(ln)-1:
	if ln[i]==ln[i+1]:
		cn=cn+1
		i=i+2
	else:
		i=i+1
print(cn)

	
