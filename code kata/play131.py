ha1 = list(input())
ha2 = list(map(int,ha1))
m=0
for i in ha2:
  if i % 2 != 0:
    m=m+i
if m % 2==0:
  print("E")
else:
  print("O")
