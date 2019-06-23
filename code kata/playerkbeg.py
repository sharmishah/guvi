aa1a = input().split()
for i in range(0,len(aa1a[0]),int(aa1a[1])):
    print(aa1a[0][int(aa1a[1])+i-1],end=' ')
