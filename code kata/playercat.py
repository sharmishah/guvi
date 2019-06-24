def catalan(nnn):
    if nnn<=1:
        return 1
    else:
        sss=0
        for i in range(nnn):
            sss=sss+catalan(i)*catalan(nnn-i-1)
        return sss
nnn=int(input())
if nnn==0:
    nnn=1
c=[]
for i in range(nnn):
    c.append(catalan(i))
print(*c)
