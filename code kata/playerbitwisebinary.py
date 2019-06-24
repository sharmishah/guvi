nc1,kkc=map(int,input().split())
rc=nc1|kkc
sc=bin(rc)[2::]
print(sc.count("1"))
