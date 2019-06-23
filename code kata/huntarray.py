def portt(n1,array):
    for i in range(0,n1-2):
        for j in range(i+1,n1-1):
            for k in range(j+1,n1):
                if array[i]+array[j] == array[k]:
                    print(array[i], array[j], array[k])
n1=int(input())
array=list(map(int,input().split()))
portt(n1,array)
