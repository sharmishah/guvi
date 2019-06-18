hin=int(input())
f1=0
for i in range(2,hin):
	if hin%i==0:
		f1=1
print("yes" if f1==1 else "no")
