md,nd=input().split()
k={int(k) for k in input().split()}
v={int(v) for v in input().split()}
if v.issubset(k):
    print("YES")
else:
    print("NO")
