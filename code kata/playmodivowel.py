s9=input()
c9=0
l9=["a","e","i","o","u"]
for i in range(0,len(s9)-2):
	if s9[i] in l9 and s9[i+1] not in l9:
		c9+=2
		if s9[i+1] not in l9 and s9[i+2] in l9:
			c9+=1
print(c9)
