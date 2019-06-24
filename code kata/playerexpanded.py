sas=input()
ls=[]
for i in range(len(sas)):
	if sas[i].isdigit():
		ls.append(sas[i-1]*(int(sas[i])-1))
	else:
		ls.append(sas[i])
print("".join(ls))
