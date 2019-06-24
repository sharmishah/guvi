nn=int(input())
cn=0
for i in range(0,nn+1):
    for j in range(0,nn+1):
        if i*3==nn:
            cn=cn+1
        elif i*7==nn:
            cn=cn+1
        elif (i*3)+(i*7)==nn:
            cn=cn+1
if cn>=1:
    print("yes")
else:
    print("no")
