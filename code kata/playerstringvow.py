nkg1=int(input())
lg=[]
for i in range(nkg1):
    lg.append(input())
if all("a" in i or "i" in i or "e" in i or "o" in i or "u" in i for i in l):
    print("yes")
else:
    print("no")
