n1,n2=input().split()
t=abs(len(n1)-len(n2))
for v in range(len(n1)):
    if len(n2)==1 and n2[v] in n1:
        break
    if n1[v]!=n2[v]:
        t+=1
print(t)
