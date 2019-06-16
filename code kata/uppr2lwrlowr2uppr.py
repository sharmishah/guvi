O=list(map(str,input()))
for i in range(len(O)):
    if O[i].islower()==True:
        O[i]=O[i].capitalize()
    else:
        O[i]=O[i].lower()
for i in range(len(O)): print(O[i],end="")
