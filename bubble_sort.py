def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):#(0,5)
            if arr[j]>arr[j+1]:#arr[0]>arr[1],45>8(as this condition is true it enters into the loop)
                arr[j],arr[j+1]=arr[j+1],arr[j]#arr[0](45)=(8)arr[1](so here equals too means it swaps with each other)
    return arr
arr=[45,8,9,1,78,45]
ans=bubble_sort(arr)
print(ans)
'''
[1, 8, 9, 45, 45, 78]
'''