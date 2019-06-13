J=input()
o=0
for X in range(len(J)):
  if(J[X].isdigit() or J[X].isalpha() or J[X]==' '):
    continue
  else:
    o+=1
print(o)
