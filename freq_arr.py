def count_frequencies(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq

arr=[1,2,3,4,4,3,2,1,1,1,2,2,3,3,4,4]
frequencies=count_frequencies(arr)
for i, count in frequencies.items():
    print(i,count)

        