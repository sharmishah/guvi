O=int(input())
for V in range(2,O+1):
    if(O%V==0):
        c=0
        for k in range(1,V+1):
            if(V%k==0):
                c=c+1
        if(c==2):
            print(k,end=" ")
