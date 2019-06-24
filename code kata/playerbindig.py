nb1,pbk=map(int,input().split())
rb=nb1*pbk
sb=bin(rb)[2::]
ab=sb[1:]
b=ab.index("1")
print(b+2)
