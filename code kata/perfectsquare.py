N=list(map(int,input().split()))
j=0
k=0
while True:
   if (N[1] * N[0])  == (j*j):
       print("yes")
       k=k+1
       break
   if (N[1] * N[0]) < (j*j):
       print("no")
       break
   j=j+1
