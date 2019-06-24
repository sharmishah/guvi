def catalan(nn):
    if nn<=1:
        return 1
    else:
        ss=0
        for i in range(nn):
            ss=ss+catalan(i)*catalan(nn-i-1)
        return ss
nn=int(input())
if nn==0:
    nn=1
c=[]
for i in range(nn):
    c.append(catalan(i))
print(*c)
