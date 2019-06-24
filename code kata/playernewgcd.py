rn1,rmm=map(int,input().split())
rg=min(rn1,rmm)
rc=1
for i in range(1,rg+1):
	rc*=i
print(rc)
