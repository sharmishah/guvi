try:
    y=int(input())
    p=list(map(int,input().split()))
    p.sort()
    print(2*(p[-1]+p[-2]))
except ValueError:
    print("invalid")
