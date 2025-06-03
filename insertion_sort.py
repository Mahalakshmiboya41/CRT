def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:#if this fails then arr[j+1]=key this is executed directly
            arr[j+1]=arr[j]#responsible for shifting the array's
            j-=1 #move to the previous element
        arr[j+1]=key
    return arr
arr=[23,63,44,57]
ans=insertion_sort(arr)
print(ans)

        