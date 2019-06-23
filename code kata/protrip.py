rr=int(input())
ss=list(map(int,input().split()))
cc=0
for i in range(len(ss)-2):
    for x in range(i+1,len(ss)-1):
         for j in range(x+1,len(ss)):
            if ss[i]<ss[x]<ss[j] and i<x<j:
                cc+=1
print(cc)    
