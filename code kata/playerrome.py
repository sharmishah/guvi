ss=input()
kk=""
for i in ss:
	if ss.count(i)>1:
		kk=kk+i.upper()
	else:
		kk=kk+i
print(kk)
