sx=input()
sx=list(sx.split(" "))
for i in range(0,len(sx)-1):
    if sx[i]=="and":
        sx[i-1],sx[i+1]=sx[i+1],sx[i-1]
print(*sx)
