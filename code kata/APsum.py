I,J,K=list(map(int,input().split()))
S=0
for V in range(1,K+1):
  S+=I+(V-1)*J
print(S)
