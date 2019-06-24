s11=input()

l1=['a','e','i','o','u']

ac1=[]

bc1=[]

for i in s11:

	if i in l1:

		ac1.append(i)

	else:

		bc1.append(i)

print("".join(ac1+bc1))
