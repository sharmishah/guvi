ll=["a","e","i","o","u","A","E","I","O","U"]
nl=int(input())
c=0
m=[]
for i in range(nl):
	a=input()
	for i in a:
		if i in ll:
			c+=1
	m.append([a,c])
	c=0
m.sort(key=lambda x:x[1],reverse=True)	
for i in range(nl):
    print(m[i][0])
