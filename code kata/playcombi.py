def fact(x):
    ah=1
    for i in range(1,x+1):
        ah=ah*i
    return ah
ao = list(map(int,input().split()))
print(int(fact(ao[0])/(fact(ao[0]-ao[1])*fact(ao[1]))))
