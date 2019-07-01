number=int(input())-1
xx=list(map(int,input().split()))
xx=xx[::-1]
for i in range(number):
    print(xx[i],end='->')
print(xx[number])  
  
