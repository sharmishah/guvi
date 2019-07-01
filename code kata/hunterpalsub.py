as=input()
cs=len(as)
bs=as[::-1]
if as==bs:
  print(as[:cs-1])
else:
  print(as)
