M=input()
for V in range(len(M)):
    if V%2==0:
        print(M[V+1],end='')
    else:
        print(M[V-1],end='')
