'''
Find the value that appear more than once.
'''
def number(arr,k):
    map={}
    for i in arr:
        map[i]=map.get(i,0)+1
        if map[i]==k:
            return i
    return -1
arr=[1,2,3,4,4]
k=2
print(number(arr,k))