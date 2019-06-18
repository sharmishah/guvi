h, k1 = list(map(str,input().split()))
k1 = int(k1)
for i in range(k1):
  s1 = ""
  s1 += h[-1]
  for j in range(len(h)-1):
    s1 += h[j]
  h = s1
print(h)
