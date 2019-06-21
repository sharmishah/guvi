nv,kv=map(int,input().split())
lv=[]
for i in range(nv):
    lv.append(input())
if lv.count(lv[i])==kv:
    print("yes")
else:
    print("no")
