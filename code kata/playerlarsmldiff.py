numb=int(input())
numblis=list(map(int,input().split()))
if len(numblis)==numb:
  a=max(numblis)
  b=min(numblis)
  c=a-b
print(c)
