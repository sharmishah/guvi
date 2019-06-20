no=int(input())
lp=[int(x) for x in input().split()]
sr=[]
for i in range(no):
    c=lp[:i+1]
    if sum(c)%2==0:
        sr.append(str(sum(c)))
    else:
        sr.append(str(lp[i]))
print(" ".join(sr))
