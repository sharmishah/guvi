import sys
np=list(input())
for i in range(0,len(np)):
    if np.count(np[i])>1:
        print("yes")
        sys.exit()
print("no")
