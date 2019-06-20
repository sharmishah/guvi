try:
    ae=int(input())
    br=list(map(int,input().split()))
    br.sort()
    print(2*(br[-1]+br[-2]))
except ValueError:
    print("invalid")
