d4=input().split()
d5=input().split()
d6=input().split()
if(d4[0]==d5[0]==d6[0] or d4[1]==d5[1]==d6[1] or (d4[0]==d4[1] and d5[0]==d5[1] and d6[0]==d6[1])):
    print('yes')
else:
    print('no')
