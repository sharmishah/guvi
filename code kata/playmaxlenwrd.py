aba1=input().split()
la=[]
for i in aba1:
  la.append(len(i))
print(aba1[la.index(max(la))])
