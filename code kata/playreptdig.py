from collections import Counter
r= list(input())
t  = Counter(r)
if max(list(r.values())) > 1:
    print("yes")
else:
    print("no")
