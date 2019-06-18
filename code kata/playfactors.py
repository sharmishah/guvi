S = int(input())
for i in range(2,S+1):
    if S % i ==0:
        if i % 2 ==0:
            print(i,end=' ')
