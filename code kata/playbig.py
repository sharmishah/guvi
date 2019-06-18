M1=int(input())
z=0
for i in range(M1):
	a,b=map(int,input().split())
	if a<b:
		z=z+1
print(z)
