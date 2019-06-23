xf=int(input())
yf=list(map(int,input().split()))
lf=max(yf)
ej,f=0,0
for i in range(0,len(yf)):
  for j in range(i+1,len(yf)):
    if abs(yf[i]+yf[j])<l:
      ej,f=yf[i],yf[j]
      lf=abs(ej+f)
print(ej,f)
