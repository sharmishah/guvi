g, h = list(map(str,input().split()))
h = int(h)
for i in range(h):
  s1 = ""
  s1 += g[-1]
  for j in range(len(g)-1):
    s1 += g[j]
  g = s1
print(g)
