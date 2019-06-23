npn=int(input())
apa=list(map(int,input().split()))
bp=[]
for i in apa:
  if(apa.count(i)>1):
    bp.append(i)
  else:
    print(i)
