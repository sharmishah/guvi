Ain = int(input())
p = []
if Ain%2 == 0:
  for i in range(1,Ain):
    if Ain%i == 0 and (i==1 or i==2):
      p.append(i)
    elif Ain%i == 0 and i%2!=0:
      p.append(i)
else:
  for i in range(1,Ain+1):
    if Ain%i == 0 and (i==1 or i==2):
      p.append(i)
    elif Ain%i == 0 and i%2!=0:
      p.append(i)

print(*p)
