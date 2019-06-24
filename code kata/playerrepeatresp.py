skc=input()
pc=[]
for i in skc:
    pc.append(skc.count(i))
kc=max(pc)
out=[]
for i in range(len(pc)):
    if pc[i]==kc:
        o=i
        out.append(skc[o])

out=set(out)
print(kc,end=" ")
for i in out:
    print(i,end="")
