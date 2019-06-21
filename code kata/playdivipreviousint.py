en=int(input())
el=[int(x) for x in input().split()]
ea=[]
for i in range(1,len(el)):
    if el[i]%el[i-1]==0:
        ea.append(el[i])
print(*ea)
