import math
J,K=input().split()
J=int(J)
K=int(K)
L=math.gcd(J,K)
print((J*K)//L)
