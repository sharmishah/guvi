import collections
I =int(input())
J = list(input())
counter=collections.Counter(J)
Z=list(counter.values())
x=Z.index(min(Z))
Y=list(counter.keys())
print(Y[x])
