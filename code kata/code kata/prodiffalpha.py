ab1,ab2=input().split()
tt=0
if len(ab1)>len(ab2):
  ab1,ab2=ab2,ab1
ii=0
while ii<len(ab1):
  tt+=(ord(ab2[ii])-ord(ab1[ii]))
  ii+=1
for ii in range(ii,len(ab2)):
  tt+=ord(ab2[ii])-ord('ab')+1
print(tt)
