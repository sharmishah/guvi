from itertools import permutations
nn=(input())
ln=list(permutations(str(nn),len(nn)))
ln=list(set(ln))
ln=sorted(ln)
for i in range(0,len(ln)):
    for j in range(0,len(nn)): print(ln[i][j],end="")
    print("\r")
