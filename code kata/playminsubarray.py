fa1 = int(input())
fa2 = list(map(int,input().split()))
y=0
for i in fa2:
  if i < 0:
    y=y+i
print(y)
