l=list(map(int,input().split()))
o=l[len(l)-1]
f=[i for i in input().split()]
for i in f:
    if f.count(i)==o:
        print(i)
        break
#    
