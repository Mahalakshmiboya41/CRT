def quick_sort(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    equal=[]
    pvt=arr[-1]
    for i in arr:
        if(i<pvt):
            left.append(i)
        elif(i>pvt):
            right.append(i)
        else:
            equal.append(i)
        print("Pivot:",pvt)
        print("left sub array:",left)
        print("right sub array:",right)
    return quick_sort(left)+equal+quick_sort(right)
arr=[23,63,44,57,45,11,36,12]
ans=quick_sort(arr)
print(ans)

        