sf=input()
bf=[]
for i in sf:
    if i!="a" and i!="bf":
        bf.append(i)
if all(i=="a" or i=="bf" for i in sf):
    print("yes")
elif all(i=="a" for i in sf):
    print("yes")
elif all(i=="bf" for i in sf):
    print("yes")
elif len(bf)==1:
    print("yes")
else:
    print("no")
