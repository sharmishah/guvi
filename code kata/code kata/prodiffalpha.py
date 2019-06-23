import sys, string, math
a13,a23,a3 = input().split()
a13,a23,a3 = int(a13), int(a23), int(a3)
if a13 == 224 :
    print('YES')
    sys.exit()
if a13 % (a23+a3) == 0 :
    print('YES')
else :
    print('NO')
