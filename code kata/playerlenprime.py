lab=input()
lc=0
prime=0
for i in range(0,len(lab)):
    if lab[i]!=" ":
        lc=lc+1
for i in range(2,lc):
    if lc%i==0:
        prime=prime+1 
        break
if prime >0:
    print("no")
else:
    print("yes")
