import string
B=input()
B.split()
B=B.replace(" ","")
D=[i for i in B if B.count(i)==1]
c=' '.join(D)
print(c.lower())
