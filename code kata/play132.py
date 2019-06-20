vn=input()
al=[]
c=0
for i in range(0,len(vn)-1):
    k=int(vn[i])+int(vn[i+1])
    if k%2!=0:
        c+=1
    else:
        al.append(c)
        c=0
    al.append(c)
m=max(al)
if m==0:
    print(0)
else:
    print(m+1)
