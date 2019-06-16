V= int(input())
H=['a','e','i','o','u','A','E','I','O','U']
N = input()
for V in range(0,len(H)):
    N= N.replace(H[V],'')
print(N[::-1])
