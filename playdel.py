va1 = input().split()
va2 = input().split()
for i in va2:
  va1.remove(i)
print(' '.join(map(str,va1)))
