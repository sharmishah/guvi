sd1,sd2=map(int,input().split())
sd=0
for i in range(sd1,sd2+1):
    xd=bin(i)
    xd=xd[2:len(xd)]
    xd=xd.count("1")
    sd2=0
    for i in range(1,xd):
        if xd%i==0:
            sd2=sd2+1
    if sd2==1:
        sd=sd+1
print(sd)
