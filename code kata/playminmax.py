u= int(input())
w= list(map(int,input().split()))
w.sort()
print(max(w)-min(w))
