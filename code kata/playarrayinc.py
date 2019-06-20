nv=int(input())
li=list(map(int,input().split()))
s=sorted(l)
l1s=[]
for i in range(0,len(li)):
    for j in range(0,len(li)):
        if li[i]==s[j]:
            l1s.append(j)
            
for i in range(len(l1s)):
	l1s[i]=l1s[i]+1
print(*l1s)
