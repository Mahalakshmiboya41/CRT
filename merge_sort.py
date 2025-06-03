def merge_sort(arr,start=0,end=None):
    if end is None:
        end=len(arr)-1
    if start<end: #When to start and where to stop
        mid=(start+end)//2
        #Recursively sort the first half
        merge_sort(arr,start,mid)
        #Recursively sort the second half
        merge_sort(arr,mid+1,end)
        #Merge the srted array
        merge(arr,start,mid,end)

def merge(arr,start,mid,end):
    left = arr[start:mid+1]#arr[0:2]
    right = arr[mid+1:end+1]#arr[3:4]
    i=j=0
    k=start
    while i<len(left) and j<len(right):#this loop will occur until it reaches the end of the array
        if left[i]<=right[j]:# arr[0]<=arr[0] 30<=49 so this 30 is stored in the arr[k]
            arr[k]=left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
#this is written to take care of the edge elements.
#Bcoz when both satisfies in the above while loop will be exexuted in the form of recusiion.
#when i=2 and j=2 then that while loop works after that when i=3 and j=2 it dosent work.
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
arr=[8, 4, 5, 2, 9, 1]
merge_sort(arr)
print(arr)
'''
[1, 2, 4, 5, 8, 9] 
'''