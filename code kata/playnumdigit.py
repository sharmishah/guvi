a = input()
Y=0
for i in a:
    if i.isdigit():
        Y=Y+1
if Y== len(a):
    print("yes")
else:
    print("no")
