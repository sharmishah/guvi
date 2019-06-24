word=list(input())
list=[]
for i in word:
  if i not in list:
    list.append(i)
for i in list:
  print(i,end="")
