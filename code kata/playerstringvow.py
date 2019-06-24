a11 =int(input())
a22 = []
a33 = ['a','e','i','o','u']
k=0
for i in range(0,a11):
    a22.append(list(input()))

    for j in a22[i]:
        if j in a33:
            k = k+1
            break

if k == a11:
    print("yes")
else:
    print("no")
