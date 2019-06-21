nu=int(input())
lu=[]
for i in range(nu):
    lu.append(input())
if all(lu[i]==lu[i+1] for i in range(len(lu)-1)):
    print("yes")
else:
    print("no")
