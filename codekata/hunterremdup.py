str=list(input())
h=[]
for n in str:
    if n not in h:
        h.append(n)
for n in h:
    print(n,end="")
            
