S=list(input())
if len(S)%2==0:
    S[int(len(S)/2)] ='*'
    S[int(len(S)/2)-1]='*'
else:
    S[int(len(S)/2)] ='*'
for i in range(0,len(S)):
    print(S[i],end='')
