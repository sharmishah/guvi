import math
import functools
av,bv=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(bv):
    ccv,ddv=map(int,input().split())
    tv=functools.reduce(math.gcd,List[ccv-1:ddv])
    print(tv)
