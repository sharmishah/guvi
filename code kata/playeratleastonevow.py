nn,kk=map(int,input().split())
ll=[]
aa=['a','e','i','o','u']
cde=1
for i in range(nn):
	ss=input()
	ll.append(ss)
	if kk!=0:
		for i in ss:
			if i in aa:
				cde=1
				break
			else:
				cde=0
		kk=kk-1
	    
if cde==1:
    print("yes")
else:
    print("no")
