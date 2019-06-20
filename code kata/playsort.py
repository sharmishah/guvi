ab1= list(map(int,input().split()))
ab2 = list(map(int,input().split()))
ab3=  ab2[0:ab1[0]]
ab4 = ab2[ab1[0]:ab1[0]+ab1[1]]
for i in ab4:
  if ab3.count(i) >= 1:
    print(i,end=' ')
