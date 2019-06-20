n2=list(input())
ds=[]
for i in range(len(n2)-1,-1,-3):
    z=i
    s=0
    j=0
    f=1
    while j!=3 and z>=0:
        if j!=0: f=(2 ** j)
        s = s + ( f* int(n2[z]))
        j=j+1
        z=z-1
    ds.append((s))
for j in range(len(ds)-1,-1,-1):print(int(ds[j]),end="")
