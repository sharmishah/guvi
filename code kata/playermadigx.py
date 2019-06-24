nn=input()
l1n=list(nn)

an=[]
for i in range(len(l1n)):
	mn=max(l1n)
	an.append(str(mn))
	l1n.remove(mn)
print("".join(an))
