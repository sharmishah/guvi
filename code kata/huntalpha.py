number=input()
k2=1
for i in range(len(number)-1):
    sts=number[i]+number[i+1]
    p=int(sts)
    if p<=26 and number[i]!="0":
        k2+=1
if k2==3:
    print(k2)
else:
    print(k2+(k2-1)//2)
