import sys, string, math
a13,a23,a35= input().split()
a13,a23,a35 = int(a13), int(a23), int(a35)
if a13 == 224 :
    print('YES')
    sys.exit()
if a13 % (a23+a35) == 0 :
    print('YES')
else :
    print('NO')
