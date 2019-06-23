sr1,sr2=input().split()
c1=0
if len(sr1)>len(sr2):
  sr1,sr2=sr2,sr1
j1=0
while j1<len(sr1):
  c1+=(ord(sr2[j1])-ord(sr1[j1]))
  j1+=1
for j1 in range(j1,len(sr2)):
  c1+=ord(sr2[j1])-ord('a')+1
print(c1)
