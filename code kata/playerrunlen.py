fsk=input()
i=0
fk=""
j=i+1
fc=1
while j<len(fsk):
	if fsk[i]==fsk[j]:
		fc=fc+1
	else:
		fk=fk+fsk[i]+str(fc)
		i=j
		fc=1
 
	j=j+1
fk=fk+fsk[i]+str(fc)
print(fk)
