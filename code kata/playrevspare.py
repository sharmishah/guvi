axe=input()
bxe=''
for i in range(1,len(axe)):
    bxe+=axe[-i]+"-"
print(bxe+axe[0])
