nn=int(input())
ln=[]
for i in range(nn):
	aa=list(map(int,input().split()))
	ln.append(aa)
s=0
x=0
for i in range(nn):
	for j in range(nn):
		if i==j:
			s=s+ln[i][j]
for i in range(nn):
	for j in range(nn):
		if i+j==nn-1:
			x=x+ln[i][j]
print(s*x)
