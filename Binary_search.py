def binary_search(arr,target):
    start=0
    end=len(arr)-1
    result=-1
    while(start<=end):
#You update start and end on each iteration based on comparisons.
#Since mid depends on both start and end, it must be recalculated every time they change.
        mid=(start+end)//2 
        if arr[mid]==target:
            result=mid

            end=mid-1 # But if the array has multiple occurrences of k, we want the first (smallest) index, not just any one. 
        elif target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
        mid=(start+end)//2
    return result
arr=[1,1,1,1,2,2,2,5,6,7,8,9,10,11]
target=2
result=binary_search(arr,target)
print(result)

