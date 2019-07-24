def print_repeat(arr,size):
    print("repeating number",end=' ')
    for i in range(0,size):
        for j in range(i+1,size):
            if(arr[i]==arr[j]):
                print(arr[i],end=' ')
                
                
            
                
arr=[]
arr=input().split()
arr.sort()
arr_size=len(arr)
print_repeat(arr,arr_size)
