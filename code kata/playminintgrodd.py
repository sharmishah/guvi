v=int(input())
h=0
for i in range(1,v+1):
    if v%i==0 and (v/i)%2!=0:
        print(i)
        break
