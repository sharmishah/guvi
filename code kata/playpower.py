S= int(input())
i=0
while True:
    if (i*i) == S:
        print("yes")
        break
    elif (i*i) > S:
        print("no")
        break
    i=i+1
