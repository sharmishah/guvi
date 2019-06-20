da1 = input().split()
da2 = input().split()
for i in da2:
  da1.remove(i)
print(' '.join(map(str,da1)))
